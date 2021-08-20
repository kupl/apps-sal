CharacterArray = []
IntegerArray = []
for II_II in range(eval(input())):
    n = eval(input())
    for KK_KK in range(n):
        (cof, exp) = list(map(int, input().split()))
        if exp == 0:
            continue
        if exp > 1:
            CharacterArray.append(str(cof * exp) + 'x^' + str(exp - 1))
        if exp == 1:
            IntegerArray.append(cof * exp)
    k = sum(IntegerArray)
    if k > 0:
        CharacterArray.append(str(k))
    str1 = ' + '.join((str(e) for e in CharacterArray))
    if len(str1) >= 1:
        print(str1)
    else:
        print('0')
    CharacterArray[:] = []
    IntegerArray[:] = []
