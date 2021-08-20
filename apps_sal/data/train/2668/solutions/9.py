step_through_with = lambda s, r=__import__('re').compile('([a-zA-Z])\\1'): bool(r.search(s))
