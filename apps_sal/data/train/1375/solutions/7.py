def __(n):
    return int(str(n)[::-1])


for i in range(eval(input())):
    a = eval(input())
    print(__(a))
