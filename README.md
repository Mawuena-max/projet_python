#  Pipeline de Traduction et Analyse Protéique

Ce projet propose un pipeline automatisé en **Python** et **Bash** pour récupérer des séquences génomiques (GenBank), les traduire en séquences peptidiques et générer des statistiques visuelles sur l'occurrence des acides aminés.

##  Fonctionnalités

Le pipeline exécute les étapes suivantes :
1. **Récupération** : Téléchargement automatisé de fichiers de séquences via URL.
2. **Traitement** : Décompression des archives (`.gz`, `.zip`).
3. **Bio-informatique** : 
   - Extraction des séquences nucléotidiques d'un fichier GenBank.
   - Transcription de l'ADN en ARN.
   - Traduction de l'ARN en acides aminés (en utilisant le code génétique standard).
   - Calcul des fréquences d'apparition de chaque acide aminé.
4. **Visualisation** : Génération d'un barplot au format PDF.
##  Prérequis

- **Python 3**
- Bibliothèque Python **Matplotlib** :
  ```bash
  pip install matplotlib

#  Pipeline d'Analyse Protéique (ADN vers Acides Aminés)

Ce projet permet d'automatiser l'analyse de séquences génomiques à partir de fichiers GenBank. Il télécharge, décompresse, traduit les séquences et génère des statistiques visuelles.

## Structure du Projet

| Fichier | Description |
| :--- | :--- |
| **occurrences.sh** | Script Bash principal qui orchestre tout le pipeline. |
| **decompression.sh** | Gère l'extraction des fichiers compressés (.gz, .zip). |
| **bases2prot.py** | Coeur bio-informatique : Transcription, Traduction et Statistiques. |
| **barplot.py** | Génère un graphique (barplot) à partir des statistiques d'occurrences. |



##  Utilisation

### Lancement du pipeline complet
Pour lancer l'analyse complète à partir d'une URL de séquence (archive .gz), utilisez :

```bash
    # Donner les permissions d'exécution
    chmod +x *.sh *.py  

    # Exécuter le pipeline
    ./occurrences.sh <URL_DU_FICHIER_GENBANK>
```

### Utilisation individuelle des scripts
```bash
   # Traduire une séquence et obtenir les statistiques :
    python3 bases2prot.py ma_sequence.gb

   #Générer le graphique PDF :
    python3 barplot.py fichier_stats.txt mon_graphique.pdf
```

### Exemple de Résultat
Le pipeline produit :

Une sortie textuelle dans le terminal listant les acides aminés et leurs occurrences.

Un fichier fichier.pdf contenant un histogramme (barplot) des fréquences détectées.

## Auteurs
Mawuéna AHONDO 

Ahamed TCHATAKOURA
