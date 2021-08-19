def number(lines):
    """Returns a list with each line prepended with the line number."""
    return [f'{n}: {string}' for (n, string) in enumerate(lines, 1)]
