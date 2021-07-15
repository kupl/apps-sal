def crap(garden, bags, cap):
    # Flatten list including only cr@p and dogs
    flat = [e for line in garden for e in line if e in 'D@']
    return 'Dog!!' if 'D' in flat else 'Clean' if len(flat) <= bags * cap else 'Cr@p'
