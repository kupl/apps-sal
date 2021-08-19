def hcfnaive(a, b):
    if b == 0:
        return a
    else:
        return hcfnaive(b, a % b)


for _ in range(int(input())):
    (num1, num2) = map(int, input().split(' '))
    print(hcfnaive(num1, num2))
