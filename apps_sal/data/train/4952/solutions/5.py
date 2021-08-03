class partial_keys(dict):
    def __getitem__(self, key):
        keys = sorted(k for k in self.keys() if k.startswith(key))
        if keys:
            return super().__getitem__(keys[0])
