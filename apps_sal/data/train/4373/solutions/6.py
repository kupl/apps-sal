def count_smileys(arr):
    smiles = set([a + b + c for a in ":;" for b in ['', '-', '~'] for c in ")D"])
    return len([1 for s in arr if s in smiles])
