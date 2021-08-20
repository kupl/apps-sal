import sys
test = int(input())
sol = []
for i in range(test):
    j = list(map(int, input().strip().split(' ')))
    (n, d) = (j[0], j[1])
    digits = list(str(n))
    for i in range(len(digits) - 1, -1, -1):
        first = 0
        if i < len(digits) - 1:
            if int(digits[i]) > int(digits[i + 1]):
                first = 1
        if int(digits[i]) >= d or first == 1:
            digits.append(str(d))
            del digits[i]
    str1 = ''
    sol.append(str1.join(digits))
for i in range(test):
    print(int(sol[i]))
