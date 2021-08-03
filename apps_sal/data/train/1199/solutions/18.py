t = int(input())
for z in range(t):
    s, n = map(int, input().split())
    if(s == 1):
        print("1")
        continue
    result = 0
    i = 0
    result = result + s // (n)
    mod = s % n
    if(mod == 0):
        print(result)
        continue
    if(mod % 2 == 0 or mod == 1):
        result = result + 1
    else:
        result = result + 2
    print(result)
