t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, str(input()).split()))
    visited = set()
    doubles = []
    for i in arr:
        if i in visited:
            visited.remove(i)
            doubles.append(i)
        else:
            visited.add(i)
    print(len(doubles) // 2)
