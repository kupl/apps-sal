N = int(input())
seq = [int(i) for i in input().split()]


def end_lst(i):
    while i < N - 1 and seq[i] != seq[i + 1]:
        i = i + 1
    return i


def reorder(lst, start, end):
    if start == end - 1:
        return 0
    if lst[start] == lst[end]:
        for i in range(start, end + 1):
            lst[i] = lst[start]
        return (end - start) // 2

    mid = (start + end) // 2
    for i in range(start, mid + 1):
        lst[i] = lst[start]
    for i in range(mid + 1, end + 1):
        lst[i] = lst[end]
    return (end - start + 1) // 2 - 1


i, ans = 0, 0
while i < N - 1:
    if seq[i] != seq[i + 1]:
        end = end_lst(i)
        ans = max(reorder(seq, i, end), ans)
        i = end
    else:
        i += 1

print(ans)
seq = list(map(str, seq))
print(" ".join(seq))
