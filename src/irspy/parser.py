"""."""

from typing import Iterator

from selectolax.parser import HTMLParser, Node

from src.irspy.readers import read_xml_file


class IRSPY:
    """Parse IRS 990 Forms."""

    def __init__(self, file_path: str):
        """Init."""
        xml = read_xml_file(file_path)
        self.tree = HTMLParser(xml)

    def __repr__(self) -> str:
        """Repr."""
        return f"IRSPY({self.tree})"

    def get_root(self) -> Node:
        """
        Get root.

        Returns:
            Node: Root node.
        """
        return self.tree.root

    def get_tree(self) -> str:
        """
        Get tree.

        Returns:
            str: HTML representation of the page.
        """
        return self.tree.html

    def get_tags(self, tag_name: str) -> list[Node]:
        """
        Get tags.

        Args:
            tag_name (str): Name of the tag. (e.g. `ReturnTs`)

        Returns:
            list[Node]: A list of tags that match specified name.
        """
        return self.tree.tags(tag_name)

    def get_nodes(self) -> Iterator[Node]:
        """
        Get tree nodes.

        Returns:
            _type_: _description_
        """
        return self.tree.root.traverse()





    def parse(self) -> None:
        """Return parsed tree."""



