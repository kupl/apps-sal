def number(lines):
    new_lines = [
        ": ".join([str(i + 1), line]) for i, line in enumerate(lines)
    ]

    return new_lines
