# cook your dish here
tc = int(input())
while tc > 0:
    N, K, E, M = map(int, input().split())
    sumi = []
    for i in range(N - 1):
        a = list(map(int, input().split()))
        sumi.append(sum(a))

    my_score = list(map(int, input().split()))
    my_sum = sum(my_score)

    sumi = sorted(sumi)
    answer = max(sumi[N - K - 1] + 1 - my_sum, 0)
    if answer > M:
        answer = "Impossible"
    print(answer)
    tc = tc - 1
