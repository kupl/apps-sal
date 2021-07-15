T = int(input())
for i in range(T):
        X = input()
        binary = bin(int(X) - 1)[2:]
        print(2**len(binary))
