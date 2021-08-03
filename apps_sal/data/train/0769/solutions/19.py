# cook your dish here
def l(a, b):
    if(b == 0):
        return a
    else:
        return l(b, a % b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(l(a, b))
