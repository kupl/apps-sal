n = int(input())
for i in range(n):
    input()
    sequence = input().split()
    out = []
    for num in sequence:
        if num not in out:
            out.append(num)
    print(' '.join(out))
