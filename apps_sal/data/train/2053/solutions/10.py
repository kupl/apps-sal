def main():
    (n, m) = list(map(int, input().split()))
    bs = list(map(int, input().split()))
    gs = list(map(int, input().split()))
    num_sweets = m * sum(bs)
    b = sorted(bs)
    del bs
    remaining_slots = [m - 1] * n
    for (j, g) in enumerate(gs):
        lval_index = n - 1
        while lval_index >= 0:
            if b[lval_index] > g:
                return -1
            if b[lval_index] == g or remaining_slots[lval_index]:
                break
            lval_index -= 1
        if lval_index < 0:
            return -1
        else:
            b_val = b[lval_index]
            if b_val != g:
                remaining_slots[lval_index] -= 1
                num_sweets = num_sweets + (g - b_val)
    return num_sweets


num_sweets = main()
print(num_sweets)
