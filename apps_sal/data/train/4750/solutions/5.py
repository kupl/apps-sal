def flatten(lst):
    return [item for sublist in [seq if isinstance(seq, list) else [seq] for seq in lst] for item in sublist]
