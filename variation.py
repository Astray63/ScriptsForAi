import cv2
import numpy as np
from PIL import Image, ImageEnhance
import random
import os

# Répertoires contenant les images et les labels
image_dir = "full/"
output_dir = "generated_images/"
label_dir = "full_labels/"
output_label_dir = "generated_labels/"
os.makedirs(output_dir, exist_ok=True)
os.makedirs(output_label_dir, exist_ok=True)

# Nombre de variations à générer pour chaque image
num_variations = 50

# Fonctions pour créer les variations
def rotate_image(image):
    angle = random.randint(-30, 30)
    return image.rotate(angle)

def adjust_brightness(image):
    enhancer = ImageEnhance.Brightness(image)
    factor = random.uniform(0.7, 1.3)
    return enhancer.enhance(factor)

def adjust_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    factor = random.uniform(0.7, 1.3)
    return enhancer.enhance(factor)

def add_noise(image):
    np_img = np.array(image)
    row, col, ch = np_img.shape
    mean = 0
    var = 10
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = np_img + gauss
    return Image.fromarray(np.uint8(np.clip(noisy, 0, 255)))

# Parcourir toutes les images du répertoire
for filename in os.listdir(image_dir):
    if filename.endswith(".png"):
        image_path = os.path.join(image_dir, filename)
        label_path = os.path.join(label_dir, os.path.splitext(filename)[0] + ".txt")

        # Vérifier si le fichier de label correspondant existe
        if not os.path.exists(label_path):
            print(f"Label file not found for {filename}. Skipping.")
            continue

        # Charger l'image originale
        image = Image.open(image_path)
        img_width, img_height = image.size

        # Lire le fichier de label correspondant
        with open(label_path, 'r') as label_file:
            labels = label_file.readlines()

        # Générer les variations pour chaque image
        for i in range(num_variations):
            transformed_image = image

            # Appliquer des transformations aléatoires
            if random.choice([True, False]):
                transformed_image = rotate_image(transformed_image)

            if random.choice([True, False]):
                transformed_image = adjust_brightness(transformed_image)

            if random.choice([True, False]):
                transformed_image = adjust_contrast(transformed_image)

            if random.choice([True, False]):
                transformed_image = add_noise(transformed_image)

            # Nommer l'image sauvegardée en fonction du fichier original
            base_name = os.path.splitext(filename)[0]
            img_save_path = f"{output_dir}/{base_name}_variation_{i}.png"
            transformed_image.save(img_save_path)

            # Copier le fichier de label original et le sauvegarder pour la nouvelle image
            label_save_path = f"{output_label_dir}/{base_name}_variation_{i}.txt"
            with open(label_save_path, 'w') as new_label_file:
                new_label_file.writelines(labels)

print(f"{num_variations} variations ont été générées pour chaque image dans les dossiers {output_dir} et {output_label_dir}")
