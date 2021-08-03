graph = [
    {"0": 0, "1": 1},
    {"1": 1, "0": 2},
    {"0": 3, "1": 1},
    {"1": 1, "0": 4},
    {"1": 1, "0": 0}
]
for i in range(0, int(input())):
    S = input()
    N = len(S)
    currentIndex = 0
    for i in range(0, N):
        currentIndex = graph[currentIndex][S[i]]
    if currentIndex == 4:
        print("YES")
    else:
        print("NO")
