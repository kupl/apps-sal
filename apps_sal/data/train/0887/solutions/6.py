
def calculate_min_path(A, B):
    if A[0] != 0 or B[n - 1] != 0:
        return False

    if A[n - 1] != B[0]:
        return False

    for i in range(1, n - 1):
        a, b, c = A[i], A[n - 1], B[i]
        if a + b < c or a + c < b or b + c < a or a * b * c == 0:
            return False
    return True


t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if calculate_min_path(A, B):
        print("Yes")
    else:
        print("No")
