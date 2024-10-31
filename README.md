# Projet : Outils de Prétraitement et Conversion de Données pour la Détection d'Objets

Ce dépôt regroupe divers scripts pour le traitement et la préparation des données d'entraînement pour des modèles de détection d'objets. Il inclut des outils pour renommer des fichiers, augmenter des données, convertir des annotations, et traiter des vidéos avec YOLO.

## Structure des Scripts

- `rename.py` : Renomme les fichiers d'un répertoire, en suivant un format spécifique.
- `variation.py` : Génère des variations d'images (rotation, luminosité, contraste, bruit) et leurs annotations associées.
- `video.py` : Applique un modèle YOLOv8 personnalisé pour détecter des objets dans une vidéo.
- `yolotococo.py` : Convertit des annotations de détection d'objets du format YOLO vers le format COCO.
- `coco.py` : Modifie les IDs d'images dans un fichier d'annotations COCO pour qu'ils soient consécutifs.
