import os
import time
from ultralytics import YOLO
import cv2
import numpy as np

# Chemin de la vidéo (modifie avec le chemin réel de ta vidéo)
video_path = r'C:\Users\Zeyko\Desktop\IA\wakfu.mp4'
video_path_out = '{}_out.mp4'.format(video_path)

# Ouvrir la vidéo d'entrée
cap = cv2.VideoCapture(video_path)

# Vérifier si la vidéo s'ouvre correctement
if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

# Lire la première frame
ret, frame = cap.read()

# Vérifier si la première frame a été lue correctement
if frame is None:
    print("Erreur : Impossible de lire la vidéo.")
    exit()

# Récupérer la hauteur, la largeur et les canaux de l'image (frame)
H, W, _ = frame.shape

# Définir l'écrivain vidéo pour la vidéo de sortie
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Charger le modèle YOLOv8 personnalisé
model_path = r'C:\Users\Zeyko\Desktop\IA\runs\detect\train4\weights\best.pt'
model = YOLO(model_path)

# Définir un seuil de détection
threshold = 0.5

# Lire et traiter la vidéo frame par frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Appliquer la détection avec le modèle YOLO
    results = model(frame)

    # Annoter la frame avec les résultats
    annotated_frame = results[0].plot()

    # Écrire la frame annotée dans la vidéo de sortie
    out.write(annotated_frame)

    # Afficher la frame annotée
    cv2.imshow('YOLOv8 Detection', annotated_frame)

    # Quitter la boucle si 'q' est pressé
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
out.release()
cv2.destroyAllWindows()
