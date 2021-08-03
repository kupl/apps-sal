# cook your dish here

for _ in range(int(input())):
    k = int(input())
    if k == 1:
        print("*")
        continue
    for i in range(k):
        for j in range(2 * (k - 1)):
            if i == 0:
                print(" " * (k - 2), end=" ")
                print("*", end="")
                break
            elif i == k - 1:
                print("*" * (2 * k - 1))
                break
            if j == k - i - 1 or j == k + i - 1:
                print("*", end="")
            else:
                print(end=" ")
        print()
