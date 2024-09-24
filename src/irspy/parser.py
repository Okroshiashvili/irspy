from selectolax.parser import HTMLParser


class Parse:
    def __init__(self, xml: str):
        self.tree = HTMLParser(xml)

    def get_text(self):
        return self.tree.css_first("p").text()
