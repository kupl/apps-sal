import sys
input = sys.stdin.readline

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    MAXl = [A[-1]]
    for i in range(1,N-1):
        MAXl.append(max(MAXl[i-1],A[-i-1]))
    MAXl.reverse()
    count = 0
    profit = 0
    for i in range(N-1):
        p = MAXl[i]-A[i]
        if p == profit:
            count += 1
        elif p > profit:
            profit = p
            count = 1

    print(count)

def __starting_point():
    main()
__starting_point()
