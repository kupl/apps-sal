def flatten_me(lst):
    return [v for sub in [e if type(e) == list else [e] for e in lst] for v in sub]
