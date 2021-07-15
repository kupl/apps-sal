
def partial_keys(d):
    class Dct(dict):
        def __getitem__(self,pk):
            k = min((k for k in self if k.startswith(pk)), default=None)
            return k if k is None else super().__getitem__(k)
    return Dct(d)
