from re import sub


def format_poem(poem):
    return sub(r"(?<=\.)\s", "\n", poem)
