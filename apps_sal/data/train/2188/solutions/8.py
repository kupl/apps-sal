cnt = [0]*262200
trans = str.maketrans('0123456789', '0101010101')
t = int(input())
for _ in range(t):
    o, a = input().split()

    if o == '+':
        cnt[int(a.translate(trans), 2)] += 1
    elif o == '-':
        cnt[int(a.translate(trans), 2)] -= 1
    else:
        print(cnt[int(a, 2)])

