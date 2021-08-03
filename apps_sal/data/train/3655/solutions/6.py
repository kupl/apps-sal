import itertools


def my_crib(n):
    """Return an ASCII art house with 'n' floors."""
    def format(chars, fill_width):
        return ("{chars[0]}{chars[2]:{chars[1]}>{width}}"
                .format(chars=chars, width=fill_width + 1)
                .center(2 * n + 2))
    return "\n".join(itertools.chain(
        (format('/ \\', 2 * i) for i in range(n)),
        (format('/_\\', 2 * n), ),
        (format("| |", 2 * n) for _ in range(n - 1)),
        (format('|_|', 2 * n), ),
    ))
