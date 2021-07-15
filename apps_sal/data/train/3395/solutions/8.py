remove_duplicate_words=lambda s:(lambda x:' '.join(e for i,e in enumerate(x)if e not in x[:i]))(s.split())
