from textual.app import App
from textual.widgets import Header, Footer, ListView, ListItem, Label

class ThreadsCLI(App):

    CSS = """
    Screen {
        layout: vertical;
    }

    ListView {
        height: 1fr;
    }
    """

    def compose(self):
        yield Header()

        posts = ListView(
            ListItem(Label("@openai  GPT-5.5 released")),
            ListItem(Label("@linux   Debian 13 is out")),
            ListItem(Label("@NASA    Webb telescope update")),
            ListItem(Label("@friend  Finished my project!")),
        )

        yield posts
        yield Footer()

if __name__ == "__main__":
    ThreadsCLI().run()
