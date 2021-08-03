
# def DecimaltoBinary():
#     N = int(input())
#     binary = bin(N)
#     setbits = [ones for ones in binary[2:] if ones=='1']
#     print(len(setbits))


# cook your dish here
t = int(input())
for i in range(t):
    N = int(input())
    print(bin(N).count("1"))
