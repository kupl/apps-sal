def min_changes(a, n):

    # To store the inversions required
    # to make the array {1, 0, 1, 0, 1, 0, 1, ...}
    # and {0, 1, 0, 1, 0, 1, 0, ...} respectively
    ans_a = 0
    ans_b = 0

    # Find all the changes required
    for i in range(n):
        if (i % 2 == 0):
            if (a[i] == 0):
                ans_a += 1
            else:
                ans_b += 1

        else:
            if (a[i] == 0):
                ans_b += 1
            else:
                ans_a += 1

    # Return the required answer
    return min(ans_a, ans_b)


for _ in range(int(input())):
    n = int(input())
    s = input()
    s = list(s)
    s = [int(x) for x in s]
    print(min_changes(s, len(s)))
