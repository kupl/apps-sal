class Random:
    """A shitty pseudo random number generator."""

    def __init__(self, seed):
        """Initilize with 'seed'."""
        self.seed = seed

    def random(self):
        """Generate a pseudo random number x (0.0 <= x < 1.0)."""
        self.seed = self.seed * 1103515245 + 12345
        return self.seed // 65536 % 32768 / 32768

    def randint(self, start, end):
        """Generate a pseudo random integer x ('start' <= x <= 'end')."""
        return start + int(self.random() * (end - start + 1))
