#!/bin/bash
#Mawuéna AHONDO & Ahamed TCHATAKOURA

decompress() {
    # Vérifier le nombre d'arguments
    if [ $# -ne 1 ]; then
        echo "Usage: $0 <fichier>"
        return 1
    fi

    file="$1"

    # Vérifier si le fichier existe
    if [ ! -e "$file" ]; then
        echo "Erreur: Le fichier '$file' n'existe pas."
        return 1
    fi

    # Déterminer l'extension du fichier
    extension="${file##*.}"

    # Décompresser le fichier si nécessaire
    case "$extension" in
        gz)
            gunzip -k "$file"
            ;;
        zip)
            unzip -d "${file%.zip}" "$file"
            ;;
        *)
            echo "$file"
            ;;
    esac

    # Stocker le code de sortie de la commande de décompression
    code_retour=$?

    # Vérifier si la décompression a réussi
    if [ $code_retour -ne 0 ]; then
        echo "Erreur: Impossible de décompresser le fichier '$file'."
        return 1
    fi
}

# Appel de la fonction avec le premier argument passé au script
decompress "$1"
