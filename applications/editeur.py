import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys
import os


def ouvrir_editeur(fenetre_principale, fichier=None):
    fen = tk.Toplevel(fenetre_principale)
    fen.title("Éditeur - IbrahPerso 1")
    fen.geometry("850x600")

    fichier_actuel = [fichier]

    zone = tk.Text(
        fen,
        font=("Consolas", 12),
        undo=True
    )
    zone.pack(fill="both", expand=True)

    def ouvrir():
        chemin = filedialog.askopenfilename(
            filetypes=[
                ("Fichiers Python", "*.py"),
                ("Fichiers texte", "*.txt"),
                ("Tous les fichiers", "*.*")
            ]
        )

        if chemin:
            fichier_actuel[0] = chemin

            try:
                with open(chemin, "r", encoding="utf-8") as f:
                    contenu = f.read()

                zone.delete("1.0", "end")
                zone.insert("1.0", contenu)
                fen.title("Éditeur - " + chemin)

            except Exception as erreur:
                messagebox.showerror("Erreur", str(erreur))

    def enregistrer():
        if fichier_actuel[0] is None:
            chemin = filedialog.asksaveasfilename(
                defaultextension=".py",
                filetypes=[
                    ("Fichiers Python", "*.py"),
                    ("Fichiers texte", "*.txt"),
                    ("Tous les fichiers", "*.*")
                ]
            )

            if not chemin:
                return False

            fichier_actuel[0] = chemin

        try:
            with open(
                fichier_actuel[0],
                "w",
                encoding="utf-8"
            ) as f:
                f.write(zone.get("1.0", "end-1c"))

            fen.title("Éditeur - " + fichier_actuel[0])
            return True

        except Exception as erreur:
            messagebox.showerror("Erreur", str(erreur))
            return False

    def executer():
        if not enregistrer():
            return

        try:
            subprocess.Popen(
                [sys.executable, fichier_actuel[0]]
            )

        except Exception as erreur:
            messagebox.showerror("Erreur", str(erreur))

    def relancer_ibrahperso():
        try:
            dossier_systeme = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )

            main_py = os.path.join(
                dossier_systeme,
                "main.py"
            )

            subprocess.Popen(
                [sys.executable, main_py],
                cwd=dossier_systeme
            )

            fenetre_principale.destroy()

        except Exception as erreur:
            messagebox.showerror(
                "Erreur",
                str(erreur)
            )

    barre = tk.Frame(fen)
    barre.pack(side="top", fill="x")

    tk.Button(
        barre,
        text="📂 Ouvrir",
        command=ouvrir
    ).pack(side="left", padx=5, pady=5)

    tk.Button(
        barre,
        text="💾 Enregistrer",
        command=enregistrer
    ).pack(side="left", padx=5, pady=5)

    tk.Button(
        barre,
        text="▶ Exécuter",
        command=executer
    ).pack(side="left", padx=5, pady=5)

    tk.Button(
        barre,
        text="🔄 Relancer IbrahPerso",
        command=relancer_ibrahperso
    ).pack(side="left", padx=5, pady=5)

    if fichier:
        try:
            with open(
                fichier,
                "r",
                encoding="utf-8"
            ) as f:
                zone.insert("1.0", f.read())

            fen.title("Éditeur - " + fichier)

        except Exception as erreur:
            messagebox.showerror(
                "Erreur",
                str(erreur)
            )