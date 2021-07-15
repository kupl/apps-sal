t = int(input())

while t:
    t -= 1 
    s = input()
    count = 0
    a = 0
    d = []
    for i in s:
        if i == '<':
            d.append('<')
        elif i == '>' and d == []:
            break
        else:
            d.pop(0)
            if d == []:
                count += 2 + a
                a = 0
            else:
                a += 2
    print(count)
