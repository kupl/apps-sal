# cook your dish here
t = int(input())
c = []
for i in range(t):
    x = int(input())
    b = bin(x).replace("0b", "")
    b = str(b)
    ans = "1"
    ans += "0" * len(b)
    el = "1"
    el += "0" * (len(b) - 1)
    # print(ans)
    i = int(ans, 2)
    if(el == b):
        c.append(x)
    else:
        c.append(i)


for k in c:
    print(k)
