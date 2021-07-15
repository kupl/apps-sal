def find_gatecrashers(ps,ivs):
    return sorted(set(ps)-set(e for p in ivs for e in [p[0]]+p[1]))
