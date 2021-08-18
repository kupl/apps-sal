def covid(n, m):
    p = False
    for j in range(len(m)):
        if(m[j] == 1 and p == False):
            k = j
            p = True
        elif(m[j] == 1 and p):
            if(j - k < 6):
                return "NO"
            else:
                k = j
    return "YES"


t = int(input())
for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    print(covid(n, m))
