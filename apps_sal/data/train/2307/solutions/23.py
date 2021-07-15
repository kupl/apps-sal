def main():
    N, A, B = map(int, input().split())
    X = list(map(int, input().split()))
 
    cost = 0
    for i in range(N-1):
        distance = abs(X[i] - X[i+1])
        if distance * A < B:
            cost += distance * A
        else:
            cost += B
    print(cost)
 
def __starting_point():
    main()
__starting_point()
