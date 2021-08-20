import random
astr = input()
N = int(astr)
s = input()
sk = s.split(' ')
ml = [int(i) for i in sk]
kl = [0 for i in ml]
k = 0
for i in range(0, N):
    if kl[i] == 0:
        kl[i] = 1
        j = ml[i]
        k = k + 1
        while kl[j - 1] == 0:
            kl[j - 1] = 1
            j = ml[j - 1]
if k % 2 == 0:
    print('Petr')
else:
    print('Um_nik')
