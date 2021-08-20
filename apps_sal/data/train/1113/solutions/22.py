x = int(input())
for i in range(x):
    y = int(input())
    h = {}
    k = input()
    k = k.split(' ')
    for j in range(y):
        if not h.get(k[j]):
            h[k[j]] = 1
        else:
            h[k[j]] += 1
    number = 10000
    occur = 0
    for key in list(h.keys()):
        if h[key] > occur:
            occur = h[key]
            number = key
        elif h[key] is occur:
            if int(key) < int(number):
                number = key
    print(str(number) + ' ' + str(occur))
