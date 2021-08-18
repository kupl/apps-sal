n = int(input())
for i in range(n):
    s, w1, w2, w3 = list(map(int, input().split()))
    if(w2 > w1):
        z1 = w2
    z2 = min(w2, w3)
    if(s == w1 + w2 and w3 <= s):
        print(2)
    elif(s == w2 + w3 and w1 <= s):
        print(2)

    elif(w1 == w2 + w3 and w1 < s):
        print(2)
    else:
        print(3)
