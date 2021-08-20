testcases = int(input())
results = []
for i in range(0, testcases):
    friends = int(input())
    (l, b) = list(map(int, input().split()))
    over = False
    if b > l:
        temp = b
        b = l
        l = temp
    for counter in range(0, friends):
        if l == b:
            over = True
            break
        elif l > b:
            l = l - b
            if b > l:
                temp = b
                b = l
                l = temp
    if over:
        results.append('No')
    else:
        results.append('Yes ' + str(l * b))
for i in range(0, testcases):
    print(results[i])
