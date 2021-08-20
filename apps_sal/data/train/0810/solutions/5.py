t = int(input())
for T in range(t):
    (n, q) = list(map(int, input().split()))
    mh = [int(i) for i in input().split()]
    for i in range(q):
        temp = input()
        if int(temp[0]) == 1:
            s = int(temp.split()[1])
            tr = set()
            for j in range(s + 1):
                tr.add(mh[j])
            for j in range(s, n):
                if mh[j] not in tr and mh[j] > mh[s]:
                    print(mh[j])
                    break
            else:
                print(-1)
        else:
            th = int(temp.split()[1])
            s = int(temp.split()[2])
            mh[th] = s
