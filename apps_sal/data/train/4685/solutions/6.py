def self_descriptive(num):
    s = str(num)
    return all(int(d) == s.count(str(i)) for i, d in enumerate(s))
