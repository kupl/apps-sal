# cook your dish here
def I(): return list(map(int, input().split()))


t = I()[0]
while(t):
    t -= 1
    a, b, c, d = I()
    print(d - b, d - c, d - a)
