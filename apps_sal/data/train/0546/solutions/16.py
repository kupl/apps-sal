# def b(n):
#     str=""
#     if n>1:
#         b(n//2)
#     print(n%2,end="")
t = int(input())
for i in range(t):
    n = int(input())
    # b(n)
    binary = bin(n)
    setBits = [ones for ones in binary[2:] if ones == '1']
    print(len(setBits) - 1)
