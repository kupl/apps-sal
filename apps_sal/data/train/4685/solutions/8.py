def self_descriptive(num):
    for (i, d) in enumerate(str(num)):
        if str(num).count(str(i)) != int(d):
            return False
    return True
