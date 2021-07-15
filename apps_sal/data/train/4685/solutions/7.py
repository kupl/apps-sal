def self_descriptive(num):
    ns = str(num)
    return all(ns.count(str(i)) == int(d) for i, d in enumerate(ns))
