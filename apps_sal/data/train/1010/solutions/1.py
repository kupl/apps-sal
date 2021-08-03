for t in range(int(input())):
    n, k = list(map(int, input().split()))
    poles = list(map(int, input().split()))
    dist = list(map(int, input().split()))
    dist_btw_poles = []
    for i in range(1, n):
        dist_btw_poles.append(poles[i] - poles[i - 1])
    if dist_btw_poles.count(dist_btw_poles[0]) == n - 1:
        print(n - k)
        continue
    c = 0
    for i in range(n - k):
        if (dist_btw_poles[i] == dist[0]):
            flag = 1
            for j in range(k):
                if (dist_btw_poles[i + j] != dist[j]):
                    flag = 0
                    break
            if (flag == 1):
                c += 1
    print(c)
