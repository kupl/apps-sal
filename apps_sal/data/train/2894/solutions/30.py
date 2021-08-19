def triple_trouble(one, two, three):
    # your code here
    res = len(one)
    l = ''
    for i in range(res):
        result = one[i] + two[i] + three[i]
        l = l + result
    return l
