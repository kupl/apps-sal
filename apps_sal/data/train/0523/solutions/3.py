# cook your dish here
MOD = (10**9) + 7


def nCrModpDP(n, r, p):

    # The array C is going to store
    # last row of pascal triangle
    # at the end. And last entry
    # of last row is nCr
    C = [0] * (n + 1)

    # Top row of Pascal Triangle
    C[0] = 1

    # One by constructs remaining
    # rows of Pascal Triangle from
    # top to bottom
    for i in range(1, (n + 1)):

        # Fill entries of current
        # row using previous row
        # values
        j = min(i, r)
        while(j > 0):
            C[j] = (C[j] + C[j - 1]) % p
            j -= 1
    return C[r]

# Lucas Theorem based function that
# returns nCr % p. This function
# works like decimal to binary
# conversion recursive function.
# First we compute last digits of
# n and r in base p, then recur
# for remaining digits


def nCrModpLucas(n, r, p):

    # Base case
    if (r == 0):
        return 1

    # Compute last digits of n
    # and r in base p
    ni = int(n % p)
    ri = int(r % p)

    # Compute result for last digits
    # computed above, and for remaining
    # digits. Multiply the two results
    # and compute the result of
    # multiplication in modulo p.
    # Last digits of n and r
    return (nCrModpLucas(int(n / p), int(r / p), p)
            * nCrModpDP(ni, ri, p)) % p;


for _ in range(int(input())):

    n, k = list(map(int, input().split()))

    arr = list(map(int, input().split()))

    arr = sorted(arr)

    value = nCrModpLucas(n - 1, k - 1, MOD)

    ans = 1

    for x in range(1, n - 1):

        if (n - x - 1) >= (k - 1):

            temp1 = nCrModpLucas(n - x - 1, k - 1, MOD)
        else:
            temp1 = 0

        if x >= (k - 1):

            temp2 = nCrModpLucas(x, k - 1, MOD)
        else:
            temp2 = 0

        # print(value,ans,temp1,temp2)
        ans = (ans * (arr[x]**(value - temp2 - temp1))) % MOD

    print(ans)
