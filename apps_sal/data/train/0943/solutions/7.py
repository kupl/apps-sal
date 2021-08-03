nb_tests = int(input())
for _ in range(nb_tests):
    a, b = [int(x) for x in input().split()]
    if a <= b:
        print(a + 1)
    else:
        print(b + 1)
