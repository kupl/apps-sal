t = int(input())
for i in range(t):
    n = int(input())
    binary = bin(n)
    setBits = [ones for ones in binary[2:] if ones == '1']
    print(len(setBits) - 1)
