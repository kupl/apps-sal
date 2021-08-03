import hashlib


class Random():
    HASH_MAX = (1 << 32 * 4) - 1

    def __init__(self, seed):
        self.seed = seed

    def random(self):
        x = int(hashlib.md5(str(self.seed).encode()).hexdigest(), 16)
        self.seed += 1
        return x / self.HASH_MAX

    def randint(self, start, end):
        return start + int(self.random() * (end + 1 - start))
