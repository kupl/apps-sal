for _ in range(int(input())):
    n, m = map(int, input().split())
    lm = [int(item) for item in input().split()]
    l = [item for item in range(1, n + 1)]
    for i in lm:
        l.remove(i)
    l.sort()
    list_chef = list()
    list_assistant = list()
    for i in range(0, len(l), 2):
        list_chef.append(l[i])
    for i in range(1, len(l), 2):
        list_assistant.append(l[i])
    print(*list_chef)
    print(*list_assistant)
