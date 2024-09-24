"""Read IRS 990 Forms."""


def read_xml_file(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        return f.read()
