n, k = list(map(int, input().split()))
time = 0

ntd = 0

for i in range(k):
    mtr = list(map(int, input().split()))[1:]

    if mtr[0] == 1:
        ln = 0

        dlt = mtr[-1]
        mtr.reverse()

        for j, val in enumerate(mtr[:-1]):
            if val - mtr[j + 1] != 1:
                time += j - ln + 1
                ln = j + 1
                dlt = mtr[j + 1]

    else:
        time += len(mtr) - 1

print(time + n - dlt)
