# cook your dish here
for _ in range(int(input())):
    n = int(input())
    count = 1
    for i in range(n):
        for j in range(n):
            x = bin(count)[2:]
            x = x[::-1]
            print( x , end=" ")
            count += 1
        print()
