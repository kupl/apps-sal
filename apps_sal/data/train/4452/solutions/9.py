def maximum_product_of_parts(s):
    s = str(s)
    subs = []
    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            subs.append([int(x) for x in [s[0:i], s[i:j], s[j:]]])
    return max([x * y * z for [x, y, z] in subs])
