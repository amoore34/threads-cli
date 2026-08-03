from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widgets import Header, Footer, ListView, ListItem, Label, Static, Input

from services.loader import load_json

POSTS = load_json()

def filter_posts(search_text):
    search_text = search_text.lower()

    if search_text == "":
        return POSTS
    
    return [
        post
        for post in POSTS
        if (
            search_text in post["title"].lower()
            or search_text in post["body"].lower()
            )
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
    def __init__(self):
            super().__init__()
            
            self.visible_posts = POSTS.copy()
            self.search_text = ""

    def compose(self) -> ComposeResult:

        yield Header()
        
        yield Input(
            placeholder="Search posts...",
            id="search"
                )

        with Horizontal():

            self.feed = ListView(
                *[
                    ListItem(Label(post["title"]))
                    #for post in POSTS
                    for post in self.visible_posts
                ]
            )

            self.preview = Static(
                POSTS[0]["body"],
                id="preview"
            )

            yield self.feed
            yield self.preview

        yield Footer()

    def refresh_feed(self) -> None:
        self.feed.clear()

        for post in self.visible_posts:
            self.feed.append(
                    ListItem(Label(post["title"]))
                    )

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Update the preview when the highlighted post changes."""

        if event.item is None:
            return

        index = self.feed.index

        self.preview.update(POSTS[index]["body"]
                            )

    def on_input_changed(self, event: Input.Changed) -> None:
        
        self.search_text = event.value
        self.visible_posts = filter_posts(event.value)
    
        self.refresh_feed()


if __name__ == "__main__":
    ThreadsCLI().run()
