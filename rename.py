import os

def rename_files(directory):
    # Liste tous les fichiers dans le dossier donné
    files = os.listdir(directory)

    # Filtrer uniquement les fichiers avec extension .png
    png_files = [f for f in files if f.endswith('.png')]

    # Renommer chaque fichier avec le format "minerai X.png"
    for idx, filename in enumerate(png_files, start=21):
        # Crée le nouveau nom
        new_name = f"minerai{idx}.png"

        # Chemin complet de l'ancien et du nouveau fichier
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        # Renommer le fichier
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_name}')

# Utilisation : change 'your_directory' par le chemin du dossier contenant les fichiers
rename_files('.')
