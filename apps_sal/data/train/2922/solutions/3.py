def crap(garden, bags, cap):
    flat = [e for line in garden for e in line if e in 'D@']
    return 'Dog!!' if 'D' in flat else 'Clean' if len(flat) <= bags * cap else 'Cr@p'
