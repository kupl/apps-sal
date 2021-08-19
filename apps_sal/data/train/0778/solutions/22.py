# cook your dish here
for I in range(int(input())):
    num = int(input())
    rev = 0
    while num != 0:
        rev = (rev * 10) + (num % 10)
        num = num // 10
    print(rev)
