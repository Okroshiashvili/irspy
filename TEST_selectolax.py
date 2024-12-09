from selectolax.parser import HTMLParser


def read_xml_file(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        return f.read()



if __name__ == "__main__":
    html = read_xml_file("data/202000079349300140_public.xml")

    tree = HTMLParser(html)

    for node in tree.root.traverse():
        print(node.tag)
        # print(f"node_tag: {node.tag}, text: {node.text(strip=True)}")

    print("Done")
