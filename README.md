# Projet : Outils de Prétraitement et Conversion de Données pour la Détection d'Objets

Ce dépôt contient plusieurs scripts utiles pour préparer des ensembles de données d'entraînement pour des modèles de détection d'objets. Il inclut des outils pour l'augmentation de données, la conversion de formats d'annotations, et bien plus encore.

## Structure du Dépôt

- `data_augmentation.py` : Script pour appliquer des techniques d'augmentation d'images, comme des rotations, des recadrages, et des ajustements de luminosité.
- `yolo_to_coco.py` : Convertit des annotations de détection d'objets du format YOLO vers le format COCO.
- `visualize_annotations.py` : Visualise les annotations pour vérifier l'exactitude des fichiers d'annotations avant l'entraînement.
- `data_split.py` : Divise le dataset en ensembles d'entraînement, de validation et de test de manière aléatoire ou selon un ratio défini.

