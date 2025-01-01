import tkinter as tk
from tkinter import ttk
from api import give_data
def dysplay1():
    # Crea la finestra principale
    root = tk.Tk()
    root.title("Tabella Dettagli")
    root.configure(bg='#0000FF')  # Colore di sfondo blu della finestra principale

    # Configura lo stile per il widget Treeview
    style = ttk.Style()
    style.theme_use('clam')  # Usa il tema 'clam', che è più personalizzabile

    # Configura lo stile per il Treeview
    style.configure("Custom.Treeview",
                    background="#0000FF",  # Colore di sfondo blu per la tabella
                    foreground="white",    # Colore del testo bianco
                    fieldbackground="#0000FF",  # Sfondo delle celle blu
                    bordercolor="white",   # Colore del bordo bianco
                    borderwidth=2)         # Spessore del bordo
    style.configure("Custom.Treeview.Heading",
                    background="#0000FF",  # Sfondo blu per l'intestazione
                    foreground="white",    # Colore bianco per il testo nell'intestazione
                    bordercolor="white",   # Bordi bianchi per l'intestazione
                    borderwidth=2)         # Bordi con spessore 2

    # Mappa lo stile per le righe selezionate
    style.map("Custom.Treeview",
              background=[('selected', '#4a4a4a')],  # Colore di sfondo quando selezionato
              foreground=[('selected', 'white')])     # Colore del testo quando selezionato

    # Crea un widget Treeview con lo stile personalizzato
    data = give_data("people")
    tree = ttk.Treeview(root, columns=("ID", "Name", "Craft"), show='headings', style="Custom.Treeview")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Craft", text="Craft")

    # Inserisci alcuni dati di esempio
    for i, person in enumerate(data, start=1):
        tree.insert("", "end", values=(i, person['name'], person['craft']))
    # Posiziona il Treeview nel contenitore
    tree.pack(expand=True, fill='both')

    # Avvia il loop principale della finestra
    root.mainloop()

# Esegui la funzione se il file viene eseguito come script principale
if __name__ == "__main__":
    dysplay1()
