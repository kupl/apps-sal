T = int(input())
while T != 0:
    T = T - 1
    N, d = map(int, input().split())
    digits = [int(i) for i in list(str(N))]
    change = True
    digits.append(d)
    while change != False:
        change = False
        for i in range(0, len(digits) - 1):
            # print(digits)
            if digits[i] > digits[i + 1]:
                change = True
                digits.pop(i)
                digits.append(d)
                # print(digits.pop(i))
                break
    digits.pop()
    ans = ''.join(map(str, digits))
    ans = int(ans)
    print(ans)
