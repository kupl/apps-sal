(a, b, _c) = list(map(int, input().split()))
af = list(map(int, input().split()))
bf = list(map(int, input().split()))
af.sort(reverse=True)
bf.sort(reverse=True)
aflen = len(af)
bflen = len(bf)
i = 0
j = 0
cnt = 0
while i < aflen and j < bflen:
    if af[i] > bf[j]:
        cnt += 1
        i += 1
    elif af[i] < bf[j]:
        cnt -= 1
        j += 1
    else:
        i += 1
        j += 1
    if cnt > 0:
        print('YES')
        break
else:
    cnt += aflen - i
    if cnt > 0:
        print('YES')
    else:
        print('NO')
