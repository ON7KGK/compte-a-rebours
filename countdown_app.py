#!/usr/bin/env python3
"""
Application de compte à rebours - Countdown Timer
Permet de calculer le nombre de jours restants jusqu'à une date choisie
"""

import sys
from datetime import date
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QSpinBox, QPushButton, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class CountdownApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compte à Rebours")
        self.setFixedSize(650, 700)

        # Variables pour le calcul
        self.days_remaining = 0
        self.selected_date = None
        self.current_unit = "days"  # "days", "hours", "minutes", "seconds"

        # Configuration de l'interface
        self.setup_ui()

    def setup_ui(self):
        """Configure l'interface utilisateur"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(40, 40, 40, 40)
        central_widget.setLayout(main_layout)

        # Titre
        title_label = QLabel("⏰ Compte à Rebours")
        title_font = QFont()
        title_font.setPointSize(32)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        main_layout.addSpacing(20)

        # Label instruction
        instruction_label = QLabel("Choisissez une date :")
        instruction_font = QFont()
        instruction_font.setPointSize(18)
        instruction_label.setFont(instruction_font)
        instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(instruction_label)

        # Frame pour les sélecteurs de date
        date_frame = QFrame()
        date_layout = QHBoxLayout()
        date_layout.setSpacing(15)
        date_frame.setLayout(date_layout)

        # Date actuelle pour initialisation
        today = date.today()

        # Jour
        day_container = QVBoxLayout()
        day_label = QLabel("Jour:")
        day_label_font = QFont()
        day_label_font.setPointSize(14)
        day_label.setFont(day_label_font)
        day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_spin = QSpinBox()
        self.day_spin.setRange(1, 31)
        self.day_spin.setValue(today.day)
        self.day_spin.setFixedWidth(80)
        self.day_spin.setFixedHeight(40)
        spin_font = QFont()
        spin_font.setPointSize(14)
        self.day_spin.setFont(spin_font)
        self.day_spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        day_container.addWidget(day_label)
        day_container.addWidget(self.day_spin)
        date_layout.addLayout(day_container)

        # Mois
        month_container = QVBoxLayout()
        month_label = QLabel("Mois:")
        month_label.setFont(day_label_font)
        month_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.month_spin = QSpinBox()
        self.month_spin.setRange(1, 12)
        self.month_spin.setValue(today.month)
        self.month_spin.setFixedWidth(80)
        self.month_spin.setFixedHeight(40)
        self.month_spin.setFont(spin_font)
        self.month_spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        month_container.addWidget(month_label)
        month_container.addWidget(self.month_spin)
        date_layout.addLayout(month_container)

        # Année
        year_container = QVBoxLayout()
        year_label = QLabel("Année:")
        year_label.setFont(day_label_font)
        year_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.year_spin = QSpinBox()
        self.year_spin.setRange(2024, 2100)
        self.year_spin.setValue(today.year)
        self.year_spin.setFixedWidth(100)
        self.year_spin.setFixedHeight(40)
        self.year_spin.setFont(spin_font)
        self.year_spin.setAlignment(Qt.AlignmentFlag.AlignCenter)
        year_container.addWidget(year_label)
        year_container.addWidget(self.year_spin)
        date_layout.addLayout(year_container)

        main_layout.addWidget(date_frame, alignment=Qt.AlignmentFlag.AlignCenter)

        main_layout.addSpacing(20)

        # Bouton de calcul
        self.calc_button = QPushButton("Calculer le compte à rebours")
        button_font = QFont()
        button_font.setPointSize(16)
        self.calc_button.setFont(button_font)
        self.calc_button.setFixedHeight(50)
        self.calc_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.calc_button.clicked.connect(self.calculate_countdown)
        self.calc_button.setStyleSheet("""
            QPushButton {
                background-color: #3B8ED0;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #2E72B4;
            }
            QPushButton:pressed {
                background-color: #1F5A8C;
            }
        """)
        main_layout.addWidget(self.calc_button)

        main_layout.addSpacing(10)

        # Frame pour les résultats
        result_frame = QFrame()
        result_frame.setStyleSheet("""
            QFrame {
                background-color: #E8E8E8;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        result_layout = QVBoxLayout()
        result_layout.setSpacing(10)
        result_layout.setContentsMargins(20, 20, 20, 20)
        result_frame.setLayout(result_layout)

        # Label de résultat
        self.result_label = QLabel("Entrez une date et cliquez sur calculer")
        result_font = QFont()
        result_font.setPointSize(16)
        self.result_label.setFont(result_font)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setWordWrap(True)
        self.result_label.setStyleSheet("color: #666666; background-color: transparent;")
        self.result_label.setMinimumHeight(50)
        result_layout.addWidget(self.result_label)

        # Label pour le nombre de jours (cliquable)
        self.days_label = QLabel("")
        days_font = QFont()
        days_font.setPointSize(48)
        days_font.setBold(True)
        self.days_label.setFont(days_font)
        self.days_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.days_label.setStyleSheet("background-color: transparent; cursor: pointer;")
        self.days_label.setMinimumHeight(100)
        self.days_label.setCursor(Qt.CursorShape.PointingHandCursor)
        self.days_label.mousePressEvent = self.toggle_unit
        result_layout.addWidget(self.days_label)

        # Label d'instruction pour le clic
        self.hint_label = QLabel("")
        hint_font = QFont()
        hint_font.setPointSize(12)
        hint_font.setItalic(True)
        self.hint_label.setFont(hint_font)
        self.hint_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hint_label.setStyleSheet("color: #999999; background-color: transparent;")
        result_layout.addWidget(self.hint_label)

        main_layout.addWidget(result_frame)
        main_layout.addStretch()

    def calculate_countdown(self):
        """Calcule le nombre de jours jusqu'à la date sélectionnée"""
        try:
            # Récupération des valeurs
            day = self.day_spin.value()
            month = self.month_spin.value()
            year = self.year_spin.value()

            # Création de la date
            self.selected_date = date(year, month, day)
            today = date.today()

            # Calcul de la différence
            delta = self.selected_date - today
            self.days_remaining = delta.days

            # Réinitialiser l'unité à "jours"
            self.current_unit = "days"

            # Mise à jour de l'affichage
            self.update_display()

        except ValueError:
            self.result_label.setText("Erreur : Date invalide. Vérifiez les valeurs.")
            self.result_label.setStyleSheet("color: #FF3333; background-color: transparent;")
            self.days_label.setText("")
            self.days_label.setStyleSheet("background-color: transparent;")
            self.hint_label.setText("")

    def update_display(self):
        """Met à jour l'affichage selon l'unité choisie"""
        if self.days_remaining < 0:
            self.result_label.setText("Cette date est déjà passée !")
            self.result_label.setStyleSheet("color: #FF3333; background-color: transparent;")
            self.days_label.setText("")
            self.days_label.setStyleSheet("background-color: transparent;")
            self.hint_label.setText("")
        elif self.days_remaining == 0:
            self.result_label.setText("C'est aujourd'hui !")
            self.result_label.setStyleSheet("color: #00AA00; background-color: transparent;")
            self.days_label.setText("🎉")
            self.days_label.setStyleSheet("color: #00AA00; background-color: transparent;")
            self.hint_label.setText("")
        else:
            self.result_label.setText(f"Jusqu'au {self.selected_date.strftime('%d/%m/%Y')}")
            self.result_label.setStyleSheet("color: #333333; background-color: transparent;")

            # Calcul selon l'unité
            if self.current_unit == "days":
                if self.days_remaining == 1:
                    text = "1 jour"
                else:
                    text = f"{self.days_remaining} jours"
                color = "#3B8ED0"
                font_size = 48
            elif self.current_unit == "hours":
                hours = self.days_remaining * 24
                if hours == 1:
                    text = "1 heure"
                else:
                    text = f"{hours:,} heures".replace(",", " ")
                color = "#9B59B6"
                font_size = 42 if hours > 999 else 48
            elif self.current_unit == "minutes":
                minutes = self.days_remaining * 24 * 60
                if minutes == 1:
                    text = "1 minute"
                else:
                    text = f"{minutes:,} minutes".replace(",", " ")
                color = "#E67E22"
                font_size = 38 if minutes > 99999 else 42
            else:  # seconds
                seconds = self.days_remaining * 24 * 60 * 60
                if seconds == 1:
                    text = "1 seconde"
                else:
                    text = f"{seconds:,} secondes".replace(",", " ")
                color = "#E74C3C"
                font_size = 36 if seconds > 999999 else 40

            # Mise à jour avec taille adaptative
            days_font = QFont()
            days_font.setPointSize(font_size)
            days_font.setBold(True)
            self.days_label.setFont(days_font)
            self.days_label.setText(text)
            self.days_label.setStyleSheet(f"color: {color}; background-color: transparent;")
            self.hint_label.setText("(Cliquez pour changer d'unité)")

    def toggle_unit(self, event=None):
        """Change l'unité affichée au clic"""
        if self.selected_date is None or self.days_remaining <= 0:
            return

        # Rotation des unités : jours -> heures -> minutes -> secondes -> jours
        if self.current_unit == "days":
            self.current_unit = "hours"
        elif self.current_unit == "hours":
            self.current_unit = "minutes"
        elif self.current_unit == "minutes":
            self.current_unit = "seconds"
        else:
            self.current_unit = "days"

        self.update_display()


def main():
    """Point d'entrée principal de l'application"""
    app = QApplication(sys.argv)

    # Style de l'application
    app.setStyle('Fusion')

    window = CountdownApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
