for _ in range(int(input())):
    N = int(input())
    
    K = 1
    for i in range(N, 0, -1):
        for j in range(i):
            print(K, end="")
            K += 1
        print()
