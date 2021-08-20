def aa_percentage(protein, residue='AILMFWYV'):
    return round(100 * sum((protein.count(aa) for aa in set(residue))) / len(protein))
