def semiPrime():
    semiprimespro = []
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    for i in range(6, 201):
        for j in prime:
            if j >= i:
                break
            if i % j == 0:
                if i // j != j and i // j in prime:
                    semiprimespro.append(i)
                else:
                    break
    return semiprimespro


(semiprimespro, x, w) = (semiPrime(), 0, 0)
for _ in range(int(input())):
    n = int(input())
    for i in semiprimespro:
        if n - i in semiprimespro:
            print('YES')
            w = 0
            break
        else:
            w = 1
    if w == 1:
        print('NO')
