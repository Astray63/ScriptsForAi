import json

# Chemin vers votre fichier JSON original
input_file = r'C:\Users\Zeyko\Desktop\capchat\datasets\train\annotations\annotations_coco.json'
# Chemin vers le fichier de sortie
output_file = 'coco_modified.json'

# Charger le fichier JSON
with open(input_file, 'r') as f:
    data = json.load(f)

# Créer un dictionnaire pour associer les nouveaux IDs
id_mapping = {}
new_id = 1  # Commence les IDs à partir de 1

# Modifier les IDs dans la section "images"
for image in data["images"]:
    old_id = image["id"]
    id_mapping[old_id] = new_id  # Associe l'ancien ID au nouveau ID
    image["id"] = new_id  # Remplace l'ID par un entier
    new_id += 1

# Modifier les IDs dans la section "annotations" pour correspondre aux nouveaux IDs
for annotation in data["annotations"]:
    old_image_id = annotation["image_id"]
    if old_image_id in id_mapping:
        annotation["image_id"] = id_mapping[old_image_id]  # Remplace l'ID de l'image

# Sauvegarder le fichier JSON modifié
with open(output_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"Fichier modifié sauvegardé sous {output_file}")
