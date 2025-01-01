from pathlib import Path
from tkinter import Toplevel, Canvas, Text, PhotoImage
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\giaco\OneDrive\Documenti\Desktop\PRESEPEVIVENTE\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def open_link(url):
    """Apre il link specificato nel browser predefinito."""
    webbrowser.open(url)


def dysplay():
    """Crea una finestra secondaria."""
    window = Toplevel()  # Usa Toplevel invece di Tk
    window.geometry("586x347")
    window.configure(bg="#FFFFFF")

    # Mantieni le immagini come attributi della finestra
    window.image_image_1 = PhotoImage(
        file=relative_to_assets("image_11.png"))
    window.image_image_2 = PhotoImage(
        file=relative_to_assets("image_12.png"))

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=347,
        width=586,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    # Usa le immagini come attributi della finestra
    canvas.create_image(
        293.0,
        173.0,
        image=window.image_image_1
    )

    canvas.create_text(
        11.0,
        16.0,
        anchor="nw",
        text="🛰️ People in the space",
        fill="#7EB5DF",
        font=("Courier", 24 * -1)
    )

    canvas.create_image(
        291.0,
        186.0,
        image=window.image_image_2
    )

    canvas.create_text(
        39.0,
        56.0,
        anchor="nw",
        text="Info:",
        fill="#295DCD",
        font=("Courier", 36 * -1)
    )

    # Creazione del widget Text per il testo principale
    text_widget = Text(
        window,
        bg="#3B2079",  # Sfondo diverso
        fg="#7EB5DF",
        font=("Courier", 12),  # Dimensione font ridotta per adattare il testo
        bd=0,
        highlightthickness=0,
        wrap="word"  # Adatta automaticamente il testo alla larghezza
    )
    text_widget.place(x=56.0, y=114.0, width=500.0, height=200.0)

    # Inserimento del testo con tag per i link
    text_widget.insert("1.0", "People in Space is a PY GUI APP. MADE BY ")
    text_widget.insert("1.end", "GIACOMO ROSSI", "link1")
    text_widget.insert("1.end", " using ")
    text_widget.insert("1.end", "open-notify API", "link2")
    text_widget.insert("1.end", " which provides information about the number of people in space, their vessels, and their names. For more information on this project go to ")
    text_widget.insert("1.end", "REPO on git hub.", "link3")
    text_widget.insert("1.end", "\nAll information provided is unofficial and unverified.")

    # Configurazione tag per i link
    text_widget.tag_config("link1", foreground="#ffff00", underline=1)
    text_widget.tag_config("link2", foreground="#ffff00", underline=1)
    text_widget.tag_config("link3", foreground="#ffff00", underline=1)

    # Collegamento dei tag ai rispettivi eventi
    text_widget.tag_bind("link1", "<Button-1>", lambda e: open_link("https://github.com/Arrow-07"))
    text_widget.tag_bind("link2", "<Button-1>", lambda e: open_link("http://open-notify.org"))
    text_widget.tag_bind("link3", "<Button-1>", lambda e: open_link("https://github.com/Arrow-07/people-in-the-space"))

    # Rendi il widget Text non modificabile
    text_widget.config(state="disabled")

    window.resizable(False, False)
