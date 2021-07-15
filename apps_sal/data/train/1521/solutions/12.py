# less goooooooo
try:
    t = int(input())
except:
    return
for q in range(t):
    l = []
    n = int(input())
    score = [0] * n
    for w in range(n):
        li = list(map(int , input().split()))
        l.append(li)
    for x in range(n):
        for y in range(x+1,n):
            if l[x][0] < l[y][0] and l[x][1] > l[y][1]:
                score[x] += 2
            elif l[y][0] < l[x][0] and l[y][1] > l[x][1]:
                score[y] += 2
            else:
                score[x] += 1 
                score[y] += 1 
    score = "".join(str(e) + " " for e in score)
    print(score)
