# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    binary = bin(n)
    setb = [ones for ones in binary[2:] if ones == '1']
    print(len(setb) - 1)
