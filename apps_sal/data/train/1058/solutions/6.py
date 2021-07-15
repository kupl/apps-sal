# cook your dish here
for _ in range(int(input())):
    n = input()
    res=""
    for i in n:
        res += str(int(i)-2)
    print(res)
