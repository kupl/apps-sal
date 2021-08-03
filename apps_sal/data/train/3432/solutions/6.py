def cipher(phrase: str):
    mass = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    j = 0
    cip = []
    num = []
    x = 0
    y = 1
    z = 2
    for i in range(0, len(phrase), 3):
        num.append(x)
        if y >= 2:
            x += 1
        num.append(y)
        y += 1
        num.append(z)
        z += 1

    for i in range(0, len(phrase)):
        for j in range(0, len(mass)):
            if phrase[i] == mass[j]:
                j = j + num[i]
                cip.append(mass[j])
                break
            elif phrase[i] == " ":
                cip.append(" ")
                break

    return (''.join(cip))
