# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        name , score = map(str,input().split())
        a.append([name,score])
        b.append(score)
    a.sort(key = lambda x:x[1])
    b.sort()
    i = 0
    while True:
        p = b.count(b[i])
        if p == 1:
            print(a[i][0])
            break
        else:
            i += p
            if i >= n:
                print("Nobody wins.")
                break
        

