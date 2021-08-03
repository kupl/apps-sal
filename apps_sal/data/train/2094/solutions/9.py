n = int(input())
A = input()

ones = A.count("n")
zeroes = A.count("z")

print(*[1 for i in range(ones)], *[0 for i in range(zeroes)])
