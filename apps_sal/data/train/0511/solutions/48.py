def main():
    N = int(input())
    a = list(map(int, input().split()))
 
    total = 0
    for other in a:
        total ^= other
 
    print(*[(other ^ total) for other in a])
 
 
def __starting_point():
    main()
__starting_point()
