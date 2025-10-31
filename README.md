# Compte à Rebours ⏰

Application de compte à rebours multiplateforme pour calculer le nombre de jours, heures, minutes ou secondes jusqu'à une date choisie.

## Fonctionnalités

- 🎯 Calculer le temps restant jusqu'à une date précise
- 🔄 Basculer entre différentes unités en cliquant sur le résultat :
  - Jours
  - Heures
  - Minutes
  - Secondes
- 🎨 Interface moderne et élégante
- 💻 Compatible macOS, Windows et Linux

## Installation

### Prérequis

- Python 3.11 ou supérieur
- PyQt6

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Lancer l'application

```bash
python countdown_app.py
```

## Utilisation

1. Sélectionnez une date avec les trois champs (Jour, Mois, Année)
2. Cliquez sur "Calculer le compte à rebours"
3. Le résultat s'affiche en jours par défaut
4. Cliquez sur le nombre affiché pour changer d'unité (jours → heures → minutes → secondes)

## Télécharger les exécutables

Des exécutables précompilés sont disponibles pour chaque plateforme :

- **Windows** : `countdown-windows.exe`
- **macOS** : `countdown-macos`
- **Linux** : `countdown-linux`

Les exécutables sont générés automatiquement via GitHub Actions à chaque version.

## Compilation

Pour compiler vous-même l'application avec Nuitka :

### Windows
```bash
python -m nuitka --standalone --onefile --enable-plugin=pyqt6 --windows-console-mode=disable countdown_app.py
```

### macOS
```bash
python -m nuitka --standalone --onefile --enable-plugin=pyqt6 --macos-create-app-bundle countdown_app.py
```

### Linux
```bash
python -m nuitka --standalone --onefile --enable-plugin=pyqt6 countdown_app.py
```

## GitHub Actions

Le projet utilise GitHub Actions pour compiler automatiquement les exécutables pour toutes les plateformes.

Le workflow se déclenche :
- À chaque push sur `main` ou `master`
- À chaque création de tag `v*` (ex: `v1.0.0`)
- Manuellement depuis l'interface GitHub

### Créer une release

Pour créer une release avec les exécutables :

```bash
git tag v1.0.0
git push origin v1.0.0
```

Les exécutables seront automatiquement compilés et ajoutés à la release GitHub.

## Technologies utilisées

- **Python 3.11+**
- **PyQt6** - Interface graphique
- **Nuitka** - Compilation en exécutable natif
- **GitHub Actions** - CI/CD

## Licence

Ce projet est libre d'utilisation.
