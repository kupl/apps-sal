class partial_keys(dict):
    def __getitem__(self, key):
        keys = sorted(k for k in self.keys() if k.startswith(key))
        if keys: return dict.__getitem__(self, keys[0])
