import os
import time

def delete_files_younger_than_one_hour():
    """Supprime les fichiers du répertoire courant modifiés il y a plus d'une heure."""
    # Obtenir l'heure actuelle
    current_time = time.time()
    
    # Obtenir le répertoire courant
    current_directory = os.getcwd()
    print(f"Répertoire courant : {current_directory}\n")

    # Parcourir les fichiers dans le répertoire courant
    for entry in os.scandir(current_directory):
        if entry.is_file():
            # Récupérer le temps de modification du fichier
            file_modification_time = entry.stat().st_mtime

            # Affiche le nom et la date de modification du fichier
            file_mod_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(file_modification_time))
            print(f"Fichier : {entry.name}, Dernière modification : {file_mod_time_str}")

            # Calculer la différence en minutes
            time_difference_minutes = (current_time - file_modification_time) / 60

            # Vérifier si le fichier a été modifié il y a plus d'une heure (60 minutes)
            if time_difference_minutes < 60:
                try:
                    os.remove(entry.path)
                    print(f"Fichier supprimé : {entry.name}")
                except Exception as e:
                    print(f"Erreur lors de la suppression de {entry.name} : {e}")

if __name__ == "__main__":
    delete_files_younger_than_one_hour()
