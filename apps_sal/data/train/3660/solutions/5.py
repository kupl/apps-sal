import math

# if you look at the matrix of possible paths...
# [ 1,  1,  1,  0]
# [ 4,  3,  2,  1]
# [10,  6,  3,  1]
# [20, 10,  4,  1]
# ...the diagonals reflect Pascal's triangle.
#
# For example, 4C1 = 4, 4C2 = 6, 4C3 = 4
# Each cell (row, col) has possible paths = dC(l-row) where:
#    d = the ordinal of the diagonal (zero-indexed)
#    l = the length of the diagonal
#
# We can calculate d and l like so:
#    d = row + n - 1 - col
#    l = d + 1
#
# Combined, we get:
#    (row + n - 1 - col) C (n - 1 - col)
def count_paths(N, coords):
    row, col = coords
    if row == 0 and col == N-1:
        return 0
    
    inverse_col = N - 1 - col
    return choose(row + inverse_col, inverse_col)

# aCb = a!/(a-b)!b!
def choose(n,k):
    if k > n:
        return 0
    if k > n-k:
        k = n-k
    product = 1
    k_list = list(range(2, k+1))
    for i in range(n, n-k, -1):
        if len(k_list) > 0:
            k_index = len(k_list)-1
            k = k_list[k_index]
            if i % k == 0:
                i = i // k
                del k_list[k_index]
        product *= i
    for k in k_list:
        product //= k
    return product
