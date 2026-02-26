#!/bin/bash
# Mawuéna AHONDO & Ahamed TCHATAKOURA

# Vérifiez si le nombre d'arguments est correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL_fichier>"
    exit 1
fi

# Extraire le nom du fichier à partir de l'URL
file_name=$(basename "$1")

# Téléchargez le fichier avec wget ou curl
wget "$1" || curl -o "$file_name" "$1"

# Vérifiez si le téléchargement s'est bien déroulé
if [ $? -ne 0 ]; then
    echo "Erreur lors du téléchargement du fichier."
    exit 1
fi

# Décompressez le fichier
./decompression.sh "$file_name"

# Vérifiez si la décompression s'est bien déroulée
if [ $? -ne 0 ]; then
    echo "Erreur lors de la décompression du fichier."
    exit 1
fi

# Définir le chemin du fichier décompressé
file_path="${file_name%.gz}"

# Exécutez base2prot.py et redirigez la sortie vers un fichier temporaire
./bases2prot.py "$file_path" > base2prot_output.txt

# Appelez barplot.py avec le fichier temporaire contenant la sortie de base2prot.py
python3 barplot.py base2prot_output.txt fichier.pdf

# Supprimez les fichiers temporaires
rm "$file_path" base2prot_output.txt