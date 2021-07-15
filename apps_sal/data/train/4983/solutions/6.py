def merge(*dcts):
    return {k: [dct[k] for dct in dcts if k in dct] for dct in dcts for k in dct}
