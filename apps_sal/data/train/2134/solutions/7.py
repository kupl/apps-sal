def solve():
    num_nodes = int(input())
    parents = [0] + [int(x)-1 for x in input().split()]
    S = [int(x) for x in input().split()]

    children = [[] for _ in parents]
    for child, parent in enumerate(parents):
        children[parent].append(child)

    for node in range(num_nodes):
        if S[node] == -1:
            S[node] = min((S[child] for child in children[node]), default=S[parents[node]])

    A = [None for _ in range(num_nodes)]
    A[0] = S[0]
    for node in range(1, num_nodes):
        A[node] = S[node] - S[parents[node]]
        if A[node] < 0:
            print('-1')
            return False

    print(sum(A))

solve()
    

