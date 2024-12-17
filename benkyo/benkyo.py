import reflex as rx

from rxconfig import config
from .file_parse import *


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    chapters = file_parse_incl("../jisho/Genki/","Chapter")
    return rx.container(
        rx.vstack(
            rx.text("This will be a cool frontend for my Jisho notes repository!"),
            rx.text("今ここで何もがない ¯\_(⊙_ʖ⊙)_/¯"),
            rx.text("Shoutout to さおりさん + トム・ハンクス")
        ),
        rx.text("Genki Chapters"),
        rx.foreach(chapters,genki_chapter_link)
    )


def genki_chapter_link(chapter: str):
    return rx.text(chapter)


#@rx.page(route="/genki_chapter/[num]")
#def 
app = rx.App()
app.add_page(index)
