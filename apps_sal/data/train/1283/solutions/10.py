try:
    N = 205
    seive = [0] * 205
    i = 2
    while(i * 2 < N):
        j = i * 2
        if(seive[i] == 0):

            while(j < N):
                seive[j] += 1
                j += i
        else:
            while(j < N):
                seive[j] = 10
                j += i
        i += 1

    pos = []
    for i in range(N):
        if(seive[i] == 2):
            pos.append(i)
    for _ in range(int(input())):
        n = int(input())
        s = 0
        e = len(pos) - 1
        while(s <= e):
            if(pos[s] + pos[e] > n):
                e -= 1
            elif(pos[s] + pos[e] < n):
                s += 1
            else:
                print("YES")
                break
        else:
            print("NO")
except:
    pass
