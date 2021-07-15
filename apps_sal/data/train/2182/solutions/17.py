from sys import stdin, stdout
a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
a_count = 26*[0]
b_count = 26*[0]
length = len(a)
for i in range(length):
    a_count[ord(a[i]) - ord('a')] += 1
    b_count[ord(b[i]) - ord('a')] += 1
result = length * ['a']
left = 0
right = length - 1
mina, minb, maxa, maxb = 0, 0, 25, 25
exclude = length//2
for i in range(25,-1,-1):
    if exclude <= 0:
        break
    while exclude >0 and a_count[i] !=0:
        exclude -= 1
        a_count[i] -= 1
exclude = (length + 1) // 2
for i in range(26):
    if exclude <= 0:
        break
    while exclude >0 and b_count[i] != 0:
        exclude -= 1
        b_count[i] -= 1
    
while a_count[mina] == 0 and mina < 25:
    mina += 1
while b_count[minb] == 0 and minb < 25:
    minb += 1
while a_count[maxa] == 0 and maxa > 0:
    maxa -= 1
while b_count[maxb] == 0 and maxb > 0:
    maxb -= 1
i = 0
while i < length:
    if i & 1 == 0:  # Alice 
        if mina < maxb:
            result[left] = chr(ord('a')+mina)
            left += 1
            a_count[mina] -= 1
            while a_count[mina] == 0 and mina < 25:
                mina += 1     
        else:
            result[right] = chr(ord('a') + maxa)
            right -= 1
            a_count[maxa] -= 1
            while a_count[maxa] == 0 and maxa > 0:
                maxa -= 1
    else:
        if mina < maxb:
            result[left] = chr(ord('a')+maxb)   
            left += 1
            b_count[maxb] -= 1
            while b_count[maxb] == 0 and maxb > 0:
                maxb -= 1
        else:
            result[right] = chr(ord('a') + minb)
            right -= 1
            b_count[minb] -= 1
            while b_count[minb] == 0 and minb < 25:
                minb += 1            
    i += 1
print(''.join(result))

