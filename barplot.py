#!/usr/bin/env python3
# Mawuéna AHONDO & Ahamed TCHATAKOURA
import matplotlib.pyplot as plt
import sys

def parse_input(file_path):
    """
    Parse les données d'un fichier.

    Args:
    -----
    file_path (str): Chemin vers le fichier contenant les données.

    Returns:
    --------
    dict: Un dictionnaire contenant les acides aminés et leurs occurrences.
    """
    data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) < 2:
            print("Fichier d'entrée mal formaté.")
            sys.exit(1)
        acides = lines[0].split()
        occurrences = list(map(int, lines[1].split()))

    for acide, occurrence in zip(acides, occurrences):
        data[acide] = occurrence

    return data




def generate_barplot(data, output_file):
    """
    Génère un barplot à partir des données fournies et sauvegarde le résultat dans un fichier PDF.

    Args:
    -----
    data (dict): Un dictionnaire contenant les acides aminés et leurs occurrences.
    output_file (str): Le nom du fichier PDF à générer pour sauvegarder le barplot.
    """
    acides = list(data.keys())
    occurrences = list(data.values())

    plt.bar(acides, occurrences)
    plt.xlabel('Acides Aminés')
    plt.ylabel('Occurrences')
    plt.title('Occurrences des Acides Aminés')
    plt.savefig(output_file)
    plt.close()  # Ferme la fenêtre d'affichage du graphique


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python barplot.py <fichier_sequences> <fichier_pdf>")
        sys.exit(1)

    fichier_sequences = sys.argv[1]
    fichier_pdf = sys.argv[2]

    data = parse_input(fichier_sequences)
    generate_barplot(data, fichier_pdf)
