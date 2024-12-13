"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.vstack(
            rx.text("This will be a cool frontend for my Jisho notes repository!"),
            rx.text("今ここで何もがない ¯\_(⊙_ʖ⊙)_/¯"),
            rx.text("Shoutout to さおりさん + トム・ハンクス")
        ),
    )


app = rx.App()
app.add_page(index)
