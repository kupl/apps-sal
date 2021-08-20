class Chicken:

    def __init__(self, lifespan):
        self.eggs = 300
        self.lifespan = lifespan
        self.age = lifespan

    def birthday(self):
        self.age -= 1
        self.eggs //= 10 / 8
        self.eggs = 0 if self.age == 0 else self.eggs
        return self

    def __repr__(self):
        return f'Chicken(eggs={self.eggs!r})'


def egged(n, s):
    chickens = [Chicken(s) for _ in range(3)]
    for i in range(n - 1):
        chickens = [c.birthday() for c in chickens]
        chickens.extend([Chicken(s) for _ in range(3)])
    return sum(map(lambda x: x.eggs, chickens)) if n > 0 else 'No chickens yet!'
