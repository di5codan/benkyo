import reflex as rx

from rxconfig import config

import re
from .file_parse import *


class State(rx.State):
    @rx.var
    def test(self) -> str:
        args = self.router.page.params
        chapter = args.get("genki_chapter_num", [])
        return f"Chapter number: {chapter}"


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.text("This will be a cool frontend for my Jisho notes repository!"),
            rx.text("今ここで何もがない ¯\_(⊙_ʖ⊙)_/¯"),
            rx.link("Genki Page",href="/genki"),
            rx.text("Shoutout to さおりさん + トム・ハンクス")
        ),
    )

def genki_chapter_link(chapter: str):
    #return rx.text(f"{chapter}")
    return rx.link(f"Chapter {chapter}", href=f"/genki/{chapter}")

@rx.page(route="genki")
def genki_overview():
    #chapters = file_parse_incl("jisho/Genki/","Chapter")
    chapters = list(range(0,24))
    return rx.vstack(
        rx.heading("Genki Chapters"),
        rx.foreach(chapters,genki_chapter_link)
    )

@rx.page(route="genki/[genki_chapter_num]")
def genki_chapter_page():
    #test = str(rx.State.genki_chapter_num)
    #print(rx.State.genki_chapter_num)
    #file = open(f"jisho/Genki/Chapter-{str(rx.State.genki_chapter_num)}.md","r")
    #print("ah")
    return rx.text(State.test)

app = rx.App()
app.add_page(index)
