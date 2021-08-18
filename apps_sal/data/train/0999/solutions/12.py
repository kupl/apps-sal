import string
a = string.ascii_uppercase
b = [i for i in range(1, 27)]
for _ in range(int(input())):
    k = int(input())
    if k == 1:
        print('A')
        continue

    for i in range(1, k + 1):
        if i % 2 != 0:
            print(a[:i])
        else:
            print(''.join(str(j) for j in range(1, i + 1)))
