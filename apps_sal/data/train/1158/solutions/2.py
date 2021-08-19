n = int(input())
count = 0
while n > 0:
    n -= 1
    inp = input().split(' ')[-1:][0]
    (eight, five, three, others) = (0, 0, 0, False)
    for each in inp:
        if each >= '0' and each <= '9':
            if each == '8':
                eight += 1
            elif each == '5':
                five += 1
            elif each == '3':
                three += 1
            else:
                others = True
                break
    if not others and eight >= five and (five >= three):
        count += 1
print(count)
