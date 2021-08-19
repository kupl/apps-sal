# cook your dish here
T = int(input())

for t in range(T):
    minions = []
    count = 0
    N, K = input().split()
    N = int(N)
    K = int(K)
    mini = input().split()
    for num in mini:
        if num == " ":
            continue
        else:
            minions.append(int(num))

    for minion in minions:
        M = minion + K
        if M % 7 == 0:
            count += 1
        else:
            continue
    print(count)
