# cook your dish here
n = int(input())
stringa = list(map(int, input().split()))
counter = 0
counter1 = 0
counter3 = 0
somma1 = 0
somma2 = 0
massimo = 0
massimo1 = 0
massimo3 = 0
stack = []
for par in stringa:
    if par == 1 or par == 3:
        if counter1 == 0 and par == 1:
            counter1 = 1
            somma1 = 1
            massimo1 = max(massimo1, 1)
        elif counter1 > 0:
            counter1 += 1
            somma1 += 1
            massimo1 = max(massimo1, somma1)
        if counter3 == 0 and par == 3:
            counter3 = 1
            somma3 = 1
            massimo3 = max(massimo3, 1)
        elif counter3 > 0:
            counter3 += 1
            somma3 += 1
            massimo3 = max(massimo3, somma3)
        if counter == 0:
            counter = 1
            massimo = max(massimo, 1)
        if len(stack) > 0 and par != stack[-1]:
            counter += 1
            massimo = max(massimo, counter)
        stack.append(par)
    else:
        if counter1 > 0:
            counter1 -= 1
            somma1 += 1
            massimo1 = max(massimo1, somma1)
        if counter3 > 0:
            counter3 -= 1
            somma3 += 1
            massimo3 = max(massimo3, somma3)
        appo = stack.pop()
        if len(stack) > 0 and appo == stack[-1]:
            pass
        else:
            counter -= 1
print(massimo, massimo1, massimo3)
