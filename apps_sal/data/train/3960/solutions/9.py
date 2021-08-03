def align_right(text, width):
    lines = []
    while len(text) > width:
        cut = text[:width + 1].rfind(" ")
        lines.append(text[:cut].rjust(width))
        text = text[cut + 1:]
    lines.append(text.rjust(width))
    return "\n".join(lines)
