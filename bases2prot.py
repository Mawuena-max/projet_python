#!/usr/bin/env python3
# Mawuéna AHONDO & Ahamed TCHATAKOURA
import matplotlib.pyplot as plt
import sys


geneticCode = {"Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],
               "Phe": ["UUU", "UUC"],
               "Ile": ["AUU", "AUC", "AUA"],
               "Met": ["AUG"],
               "Val": ["GUU", "GUC", "GUA", "GUG"],
               "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
               "Pro": ["CCU", "CCC", "CCA", "CCG"],
               "Thr": ["ACU", "ACC", "ACA", "ACG"],
               "Ala": ["GCU", "GCC", "GCA", "GCG"],
               "Tyr": ["UAU", "UAC"],
               "STOP": ["UAA", "UAG", "UGA"],
               "His": ["CAU", "CAC"],
               "Gln": ["CAA", "CAG"],
               "Asn": ["AAU", "AAC"],
               "Lys": ["AAA", "AAG"],
               "Asp": ["GAU", "GAC"],
               "Glu": ["GAA", "GAG"],
               "Cys": ["UGU", "UGC"],
               "Trp": ["UGG"],
               "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
               "Gly": ["GGU", "GGC", "GGA", "GGG"]}

def extract_first_sequence(file_handle):
    """Extract the complete nucleotide sequence.

    Parameters:
    ===========
    * file_handle (file handle): File handle pointing to an open GenBank file.

    Returns:
    ========
    Returns the complete nucleotide sequence as a string.
    """
    sequence = ""
    is_sequence = False
    for line in file_handle:
        if line[0:6] == "ORIGIN":
            is_sequence = True
        if is_sequence:
            sequence += line[10:].strip().replace(" ", "")
        if line.strip() == "//":
            break
    return sequence.upper()


def transcription(fragment):
    """
    Transcrit un brin d'ADN (base A T C G) en brin d'ARN (base A U C G).
    
    Args:
        fragment (str): fragment d'ADN
        
    Return:
        arn (str): fragment d'ARN
    """   # chatgpt
    # Filtrer les caractères non standard
    fragment = ''.join([c for c in fragment if c in 'ATCG'])
    
    return fragment.replace("T", "U")

def codon_to_aa(uncodon):
    """
    Renvoie le code à trois lettres d'un acide aminé correspondant au codon
    donné en argument.
    
    Args:
        uncodon (str): codon de l'ARN.
        
    Return:
        acideAmine (str): code à trois lettres de l'acide aminé correspondant.
    """        
    acideAmine = None
    identify = False
    for aa, codons in geneticCode.items():
        if uncodon in codons:
            acideAmine = aa
            identify = True
            break
            
    if not identify:
        raise ValueError("ERREUR : codon '%s' non identifié" % uncodon)

    return acideAmine

def traduction(fragment):
    """
    Traduit le brin d'ARN en séquence peptidique.
    
    Args:
        fragment (str): fragment d'ARN à traduire
        
    Returns:
        sequence (str): séquence peptidique.
    """
    #nombre de codons dans le fragment
    ncodon = len(fragment) // 3
    
    # traduction    
    sequence = ""
    n = 0
    while n < ncodon:
        codon = fragment[3*n : 3*n+3]
        # Ignorer les codons non standard ou incomplets
        if len(codon) == 3:
            aa = codon_to_aa(codon)
            if aa != "STOP":
                sequence += aa + "-"
                n += 1
            else:
                sequence += aa
                break
        else:
            # Gérer les codons incomplets ou non standard
            # Vous pouvez choisir d'ignorer, remplacer ou traiter autrement ces codons
            # Ignorer le codon s'il n'est pas valide
         continue
    return sequence
def get_stat_aa(sequence):
    """ Compte le nombre de chaque type d'acide aminé et retourne un dictionnaire """
    # liste des acides aminés sauf codon STOP
    listeaa_sequence = sequence.split("-")[:-1]
    
    # statistique
    data = dict()
    for aa in listeaa_sequence:
        naa = listeaa_sequence.count(aa)
        if naa != 0:
            data[aa] = naa
    
    return data

def affichage_acides_aminés_statistiques(data):
    """
    Affiche les acides aminés et leurs occurrences.

    Arguments :
        data : dict
            Un dictionnaire contenant les acides aminés et leurs occurrences.
    """
    acides = list(data.keys())
    occurrences = list(data.values())
    
    print(' '.join(acides))
    print(' '.join("{:^3}".format(o) for o in occurrences))

if len(sys.argv) < 2:
    print("Veuillez spécifier le nom du fichier GenBank en argument.")
    sys.exit(1)


file_name = sys.argv[1]
with open(file_name, "r") as file:
    first_sequence = extract_first_sequence(file)
    sequence_transcribed = transcription(first_sequence)
    sequence_translated = traduction(sequence_transcribed)
    data = get_stat_aa(sequence_translated)
    affichage_acides_aminés_statistiques(data)


    