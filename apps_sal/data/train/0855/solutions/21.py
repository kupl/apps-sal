count = input()
for i in range(int(count)):
    stringToConvert = input()
    for i in reversed(range(len(stringToConvert))):
        print(stringToConvert[i], end='')
    print('\n')
