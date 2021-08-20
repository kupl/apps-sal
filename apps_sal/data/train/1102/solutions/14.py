d = {2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4}
t = int(input())
res = []
for x in range(t):
    st = input()
    mul = 1
    for i in st:
        if i.isdigit() == False:
            continue
        digit = int(i)
        if digit >= 2 and digit <= 9:
            mul = mul * d[int(i)]
            mul = mul % 1000000007
        else:
            continue
    res.append(mul)
for x in res:
    print(x)
