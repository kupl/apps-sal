bin = input()

ok = 1
for i in range(len(bin)):
    if bin[i] == '0':
        bin = bin[0:i] + bin[i + 1: len(bin)]
        ok = 0
        break

if ok == 1:
    bin = bin[0:-1]

print(bin)
