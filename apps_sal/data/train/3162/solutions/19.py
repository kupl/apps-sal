def compare(s1, s2):
    clean1 = clean(s1)
    clean2 = clean(s2)
    sum1 = ord_sum(clean1)
    sum2 = ord_sum(clean2)
    return sum1 == sum2

# check for empty conditions


def clean(s):
    clean = s
    if clean == None:
        clean = ''
    for char in clean:
        if not char.isalpha():
            clean = ''
            break
    return clean


def ord_sum(s):
    ords = [ord(c.upper()) for c in s]
    return sum(ords)
