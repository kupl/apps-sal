import re


def autocorrect(input):
    auto_re = r"\b(u|you+)\b"
    return re.sub(auto_re, "your sister", input, flags=re.IGNORECASE)
