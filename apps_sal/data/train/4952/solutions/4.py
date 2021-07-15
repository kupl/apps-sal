class partial_keys(dict):
    def __getitem__(self, key):
        return next((v for k,v in sorted(self.items()) if k.startswith(key)), None)
