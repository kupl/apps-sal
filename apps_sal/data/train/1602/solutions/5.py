T = int(input())


def choc(x, A):
    sorted_A = list(A)
    sorted_A.sort()

    def dec_by_one(a): return a - 1

    while not sorted_A == [] and sorted_A[0] > 1:
        del sorted_A[:x]
        sorted_A = list(map(dec_by_one, sorted_A))

    if sorted_A == []:
        print("Possible")
    else:
        print("Impossible")


for testcase in range(T):
    n = input()
    x = int(input())
    A = [int(a) for a in input().split()]

    choc(x, A)
