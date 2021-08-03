binary = input()
index = binary.find('0')

if index != -1:
    print(binary[:index] + binary[index + 1:])
else:
    print(binary[1:])
