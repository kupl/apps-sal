# cook your dish here
n, q = map(int, input().split())
edges = 2 * (2**n - 1)
side_nodes = n + 1
top_nodes = 1
bottom_nodes = 2**n
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if query[1] == 1 or query[1] == 2:
            edges = edges * 2 + side_nodes
            top_nodes *= 2
            bottom_nodes *= 2
        elif query[1] == 3:
            edges = edges * 2 + top_nodes
            top_nodes = bottom_nodes
            side_nodes *= 2
        else:
            edges = edges * 2 + bottom_nodes
            bottom_nodes = top_nodes
            side_nodes *= 2
    else:
        print(edges % 1000000007)
