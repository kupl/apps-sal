from re import sub


def format_poem(poem):
    return sub('(?<=\\.)\\s', '\n', poem)
