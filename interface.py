import tkinter as tk
from tkinter import messagebox, ttk
import threading
import os

# On importe le moteur qu'on a construit ensemble
from S_2 import dophina_engine_11_etapes

def lancer_audit():
    url = url_entry.get().strip()
    
    if not url:
        messagebox.showwarning("Dophina 2.0 - Oups !", "Tu as oublié de taper l'adresse du site internet, mon pote !")
        return
        
    if not url.startswith("http://") and not url.startswith("https://"):
        # Petite correction automatique pour aider l'utilisateur sans le gronder
        url = "https://" + url
        url_entry.delete(0, tk.END)
        url_entry.insert(0, url)

    # Désactiver le bouton pendant le scan pour faire pro et éviter les doubles clics
    bouton_scan.config(state=tk.DISABLED, text="Analyse en cours... 🐬")
    status_label.config(text="Dophina inspecte les coulisses du site... Patientez quelques secondes.", fg="#1565C0")
    progress.start(10)
    
    # On lance l'audit dans un thread séparé pour que la fenêtre ne freeze pas (effet bugué)
    def run():
        try:
            dophina_engine_11_etapes(url, annees_simulees=3)
            
            # Revenir sur le thread principal pour mettre à jour l'interface graphique
            root.after(0, audit_termine_succes)
        except Exception as e:
            root.after(0, lambda: audit_termine_erreur(str(e)))

    threading.Thread(target=run, daemon=True).start()

def audit_termine_succes():
    bouton_scan.config(state=tk.NORMAL, text="Analyser le site 🚀")
    status_label.config(text="Analyse terminée avec succès !", fg="#2E7D32")
    progress.stop()
    
    chemin_rapport = os.path.abspath("rapport_audit.txt")
    
    # Fenêtre pop-up claire et rassurante
    messagebox.showinfo(
        "Dophina 2.0 - Terminé !", 
        f"Génial ! L'analyse de sécurisation passive est finie.\n\n"
        f"Ton rapport complet avec les solutions de blindage a été créé ici :\n"
        f"{chemin_rapport}\n\n"
        "Ouvre-le pour découvrir les chiffres clés !"
    )

def audit_termine_erreur(erreur):
    bouton_scan.config(state=tk.NORMAL, text="Analyser le site 🚀")
    status_label.config(text="L'analyse a rencontré un problème.", fg="#C62828")
    progress.stop()
    messagebox.showerror("Dophina 2.0 - Erreur", f"Impossible d'analyser le site.\nDétails : {erreur}")

# --- CONFIGURATION DE L'INTERFACE VISUELLE ---
root = tk.Tk()
root.title("Dophina 2.0 - Assistant de Sécurisation")
root.geometry("550x350")
root.configure(bg="#F4F6F9") # Fond d'écran clair et moderne
root.resizable(False, False)

# Titre Principal sympa
title_label = tk.Label(
    root, 
    text="🐬 Dophina 2.0", 
    font=("Helvetica", 24, "bold"), 
    bg="#F4F6F9", 
    fg="#0288D1"
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    root, 
    text="L'assistant malin qui vous aide à blinder votre site internet face au temps.", 
    font=("Helvetica", 10, "italic"), 
    bg="#F4F6F9", 
    fg="#546E7A"
)
subtitle_label.pack(pady=5)

# Zone de saisie de l'URL
frame_saisie = tk.Frame(root, bg="#F4F6F9")
frame_saisie.pack(pady=20)

label_url = tk.Label(frame_saisie, text="Adresse du site (URL) :", font=("Helvetica", 11), bg="#F4F6F9", fg="#37474F")
label_url.pack(anchor="w", padx=5)

url_entry = tk.Entry(frame_saisie, width=45, font=("Helvetica", 12), bd=2, relief="groove")
url_entry.insert(0, "https://www.wikipedia.org") # Exemple par défaut
url_entry.pack(pady=5, ipady=4)

# Barre de progression pro (indéterminée)
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
progress.pack(pady=10)

# Statut textuel
status_label = tk.Label(
    root, 
    text="Prêt à lancer l'analyse passive sécurisée.", 
    font=("Helvetica", 10), 
    bg="#F4F6F9", 
    fg="#78909C"
)
status_label.pack(pady=5)

# Gros bouton d'action rassurant
bouton_scan = tk.Button(
    root, 
    text="Analyser le site 🚀", 
    font=("Helvetica", 12, "bold"), 
    bg="#0288D1", 
    fg="white", 
    activebackground="#01579B", 
    activeforeground="white",
    bd=0, 
    cursor="hand2",
    command=lancer_audit
)
bouton_scan.pack(pady=15, ipadx=20, ipady=8)

# Lancement de la fenêtre
root.mainloop()