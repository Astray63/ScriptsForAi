import os
import json
from PIL import Image
from pathlib import Path

def convert_yolo_to_coco(image_dir, label_dir, output_file):
    """
    Convertit les annotations YOLO en format COCO.
    
    Args:
        image_dir (str): Chemin vers le répertoire des images
        label_dir (str): Chemin vers le répertoire des annotations YOLO
        output_file (str): Chemin du fichier JSON de sortie
    """
    # Créer la structure COCO
    coco_data = {
        "images": [],
        "annotations": [],
        "categories": [{"id": i, "name": str(i)} for i in range(9)]  # Classes 0 à 8
    }
    
    annotation_id = 0
    image_dir = Path(image_dir)
    label_dir = Path(label_dir)
    
    # Traiter chaque image
    for image_path in image_dir.glob("*.[jp][pn][g]"):  # Accepte jpg, jpeg, png
        try:
            # Extraire l'ID complet depuis le nom du fichier (en utilisant le nom complet sans extension)
            image_id = image_path.stem  
            label_path = label_dir / f"{image_id}.txt"
            
            # Vérifier si le fichier d'annotation existe
            if not label_path.exists():
                print(f"Attention : Fichier d'annotation manquant pour {image_path.name}. Chemin attendu : {label_path}")
                continue
                
            # Obtenir les dimensions de l'image
            with Image.open(image_path) as img:
                width, height = img.size
            
            # Ajouter les informations de l'image
            coco_data["images"].append({
                "id": image_id,
                "width": width,
                "height": height,
                "file_name": image_path.name
            })
            
            # Lire et convertir les annotations
            with open(label_path, "r") as file:
                for line in file:
                    try:
                        # Convertir les annotations YOLO en COCO
                        class_id, x_center, y_center, w, h = map(float, line.strip().split())
                        
                        # Convertir les coordonnées normalisées en pixels
                        x_center *= width
                        y_center *= height
                        w *= width
                        h *= height
                        
                        # Calculer les coordonnées du coin supérieur gauche
                        x = max(0, x_center - w / 2)
                        y = max(0, y_center - h / 2)
                        
                        # S'assurer que la boîte ne dépasse pas les limites de l'image
                        w = min(width - x, w)
                        h = min(height - y, h)
                        
                        # Ajouter l'annotation
                        coco_data["annotations"].append({
                            "id": annotation_id,
                            "image_id": image_id,
                            "category_id": int(class_id),
                            "bbox": [x, y, w, h],
                            "area": w * h,
                            "iscrowd": 0
                        })
                        annotation_id += 1
                        
                    except ValueError as e:
                        print(f"Erreur lors de la lecture de l'annotation dans {label_path}: {e}")
                        continue
                        
        except Exception as e:
            print(f"Erreur lors du traitement de {image_path}: {e}")
            continue
    
    # Sauvegarder en JSON avec indentation pour une meilleure lisibilité
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(coco_data, f, indent=2)
    
    print(f"Conversion terminée. {annotation_id} annotations ont été converties.")

# Utilisation du script
if __name__ == "__main__":
    image_dir = r"C:\Users\Zeyko\Desktop\capchat\generated_images"
    label_dir = r"C:\Users\Zeyko\Desktop\capchat\generated_labels"
    output_file = "annotations_coco.json"
    
    convert_yolo_to_coco(image_dir, label_dir, output_file)
