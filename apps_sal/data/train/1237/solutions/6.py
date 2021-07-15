def convert(dollars, cents, required):
    a = dollars
    b = cents
    if b >= required:
        return ((b-required, a))
    else:
        a = a-1
        b = b+100
        return ((b-required, a))

# print(convert(2, 55, 30))

for _ in range(int(input())):
    thearr = []
    a, b, c = map(int,input().split())
    thearr.append((a,b))
    max_so_far = thearr[0][0] + thearr[0][1]/100
    transform = 0
    index = 1
    count = 0
    while a+b/100 > c/100 and count < 10000:
        z = convert(a, b, c)
        sum = z[0] + z[1]/100
        if sum > max_so_far:
            max_so_far = sum
            transform = index
        thearr.append(z)
        a, b = z
        index += 1
        count += 1
        # print(thearr, a, b)

    print(transform)
    # print(thearr[:10])
