def self_descriptive(num):
    num = str(num)
    return all((num.count(str(i)) == int(d) for (i, d) in enumerate(num)))
