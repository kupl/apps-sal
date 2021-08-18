
def solve(A, n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if A[i] == A[j]:
                    if i + 1 in A and j + 1 in A:
                        return True
    return False


try:
    T = int(input())
    for l in range(T):

        n = int(input())
        path = [int(i) for i in input().strip().split(" ")]
        if solve(path, n):
            print("Truly Happy")
        else:
            print("Poor Chef")


except EOFError:
    pass
