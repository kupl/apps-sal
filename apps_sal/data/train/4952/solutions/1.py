class PartialKeysDict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._keys_list = sorted(self.keys())

    def __getitem__(self, key):
        for q in self._keys_list:
            if q.startswith(key):
                return super().__getitem__(q)


partial_keys = PartialKeysDict
