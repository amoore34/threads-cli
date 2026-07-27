from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, ListView, ListItem, Label, Static


POSTS = [
    {
        "title": "@openai",
        "body": "GPT-5.5 is now available with improvements to coding and reasoning."
    },
    {
        "title": "@linux",
        "body": "Debian has released another round of package updates."
    },
    {
        "title": "@NASA",
        "body": "Webb Telescope captures another incredible image."
    },
    {
        "title": "@friend",
        "body": "Finished building my Raspberry Pi project!"
    },
]


class ThreadsCLI(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    Horizontal {
        height: 1fr;
    }

    ListView {
        width: 35%;
        border: round green;
    }

    #preview {
        border: round cyan;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:

        yield Header()

        with Horizontal():

            self.feed = ListView(
                *[
                    ListItem(Label(post["title"]))
                    for post in POSTS
                ]
            )

            self.preview = Static(
                POSTS[0]["body"],
                id="preview"
            )

            yield self.feed
            yield self.preview

        yield Footer()


if __name__ == "__main__":
    ThreadsCLI().run()
