# Function for nth fibonacci number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1
s = []


def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program
for _ in range(1, 101):
    s.append(fibonacci(_))
s[0] = 0

# This code is contributed by Saket Modi

for _ in range(int(input())):
    n = int(input())
    # s=[0,1,1,2,3,5,8,13,21,34]
    p = 0
    for _ in range(1, n + 1):
        for __ in range(1, _ + 1):
            print(s[p], end=" ")
            p += 1
        print()
    print()
