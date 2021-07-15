n = int(input())
inp = input()
seq = inp.split(' ')
seq = [ abs(int(x)) for x in seq ]
Max = max(seq)
nxt = [0] * n
cnt = [0] * n
pos = [n] * (Max+1)
for i in range(n-1, -1, -1):
    nxt[i] = pos[seq[i]]
    pos[seq[i]] = i
for i in range(0, Max+1):
    j = pos[i]
    while(j<n):
        front = sum(cnt[0:j])
        back  = sum(cnt[j+1:n])
        if(front < back):
            seq[j] = 0 - seq[j]
        j = nxt[j]
    j = pos[i]
    while(j < n):
        cnt[j] = 1
        j = nxt[j]
#for i in range(0, n-1):
#    print(seq[i], sep=' ')
#print(seq[n-1])
inv = 0
for i in range(len(seq)):
    for j in range(i+1, len(seq)):
        if(seq[i] > seq[j]):
            inv += 1
print(inv)

