class partial_keys(dict):
    def __getitem__(self, key):
        if key in self:
            return super().__getitem__(key)
        for k in sorted(self):
            if k.startswith(key):
                return super().__getitem__(k)
