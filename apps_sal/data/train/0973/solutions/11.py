def __starting_point():
    t = int(input())
    for _ in range(t):
        n,k = map(int, input().split())
        A = [int(i) for i in input().split()]
        print(max(A) - min(A) + 2*k)
__starting_point()
