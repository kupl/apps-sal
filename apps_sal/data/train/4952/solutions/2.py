class partial_keys(dict):

    def __getitem__(self, key):
        return self.get(next((k for k in sorted(self.keys()) if k.startswith(key)), None), None)
