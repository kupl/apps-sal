def main():
    N, L = list(map(int, input().split()))
    Sn = [input() for i in range(N)]
    Sn2 = sorted(Sn)
    ans = ""
    for val in Sn2 :
        ans = ans + val
    print(ans)

def __starting_point():
    main()

__starting_point()
