for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    dpo = [0] * n
    dpe = [0] * n
    for (i, a) in enumerate(arr):
        if i > k:
            if a & 1:
                dpo[i] = max(dpo[i - 1], dpo[i - k - 1] + a)
                dpe[i] = dpe[i - 1]
            else:
                dpe[i] = max(dpe[i - 1], dpe[i - k - 1] + a)
                dpo[i] = dpo[i - 1]
        elif a & 1:
            dpo[i] = max(dpo[i - 1], a)
            dpe[i] = dpe[i - 1]
        else:
            dpe[i] = max(dpe[i - 1], a)
            dpo[i] = dpo[i - 1]
    print(dpo[-1] + dpe[-1])
