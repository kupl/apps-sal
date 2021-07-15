t = int(input())
numbers = list()

for _ in range(t):
    numbers.append(int(input()))

for n in numbers:
    for i in range(1, n):
        print(" "*(n-i), end="")
        for j in range(1, i+1):
            if i==1 or j==1 or j==i or i==n:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
    print("*" * (2*n - 1))
    
