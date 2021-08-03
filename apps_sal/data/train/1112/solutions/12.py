# cook your dish here
# cook your dish here
def solve():
    n = int(input())
    #n,m = input().split()
    #n = int(n)
    #m = int(m)
    #s = input()
    #a = list(map(int, input().split()))
    it = n
    k = 1
    for i in range(n):
        j = 0
        while j < it:
            print(k, end="")
            j += 1
            k += 1
        print("")
        it -= 1


def __starting_point():
    T = int(input())
    for i in range(T):
        #a = solve()
        #n = len(a)
        # for i in range(n):
        #   if i==n-1 : print(a[i])
        #  else: print(a[i],end=" ")
        (solve())


__starting_point()
