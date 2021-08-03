# cook your dish here

t = 0
try:
    t = int(input())
except:
    pass
for _ in range(t):
    a = input()
    b = input()

    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    count = 0
    for b_character in b:
        if b_character in a:
            i = a.find(b_character)
            a = a[:i] + a[i + 1:]
            count += 1

    print(count)
