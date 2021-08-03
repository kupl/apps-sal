def flood_fill(adj_lists, colors, i, color):
    q = set()
    q.add(i)
    while len(q) > 0:
        j = q.pop()
        if colors[j] is None:
            colors[j] = color
            for k in adj_lists[j]:
                q.add(k)


def main():
    n, k = list(map(int, input().split()))
    adj_lists = [[] for _ in range(n)]
    for _ in range(k):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        adj_lists[a].append(b)
        adj_lists[b].append(a)
    colors = [None for _ in range(n)]
    num_colors = 0
    for i in range(n):
        if colors[i] is None:
            flood_fill(adj_lists, colors, i, num_colors)
            num_colors += 1
    print(k - n + num_colors)


def __starting_point():
    main()


__starting_point()
