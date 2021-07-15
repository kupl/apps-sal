class partial_keys(dict): __getitem__ = lambda self, key: self.get(next((k for k in sorted(self.keys()) if k.startswith(key)), None), None)
