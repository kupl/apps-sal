from operator import mul, add, floordiv, sub


class Placeholder:
    num = -1

    def __init__(self, so_farr=[]):
        self.so_far = so_farr

    def __call__(self, *args):
        ds = self.unpacked()
        (priori, m) = (0, 0)
        for i in range(len(ds)):
            if ds[i] == '':
                ds[i] = args[m]
                m += 1
        i = 0
        while len(ds) > 1:
            if i < len(ds) and isinstance(ds[i], tuple):
                if ds[i][1] == priori:
                    ds[i] = ds[i][0](ds[i - 1], ds[i + 1])
                    del ds[i - 1]
                    del ds[i]
                    priori += 1
                    continue
            i += 1
            if i >= len(ds):
                i = 0
        Placeholder.num = -1
        return ds[0]

    def unpacked(self):
        ds = []
        for i in range(len(self.so_far)):
            if isinstance(self.so_far[i], Placeholder):
                ds += self.so_far[i].unpacked()
            else:
                ds += [self.so_far[i]]
        if not self.so_far:
            ds += ['']
        return ds

    def __add__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder(self.so_far + [(add, self.num), other])

    def __sub__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder(self.so_far + [(sub, self.num), other])

    def nullif(self):
        if not self.so_far:
            self.so_far.append('')

    def __mul__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder(self.so_far + [(mul, self.num), other])

    def __floordiv__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder(self.so_far + [(floordiv, self.num), other])

    def __radd__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder([other, (add, self.num)] + self.so_far)

    def __rsub__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder([other, (sub, self.num)] + self.so_far)

    def __rmul__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder([other, (mul, self.num)] + self.so_far)

    def __rfloordiv__(self, other):
        self.nullif()
        Placeholder.num += 1
        return Placeholder([other, (floordiv, self.num)] + self.so_far)


x = Placeholder()
