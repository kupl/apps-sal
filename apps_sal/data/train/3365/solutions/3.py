from re import sub

# Try to solve this challenge with the str.split() and the str.join() string methods.
# -> No


def format_poem(poem):
    return sub(r"(?<=\.)\s", "\n", poem)
