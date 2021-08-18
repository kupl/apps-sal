t = int(input())
for _ in range(t):
    stringa = input()
    a = 0
    counter = 0
    for char in stringa:
        if char == 'a':
            a += 1
    print(2**(len(stringa) - a) * (2**a - 1))
