# cook your dish here
tests = int(input())
for test in range(tests):
    n = input().strip()
    length = len(n)
    steps = length - (n.count('4') + n.count('7'))
    print(steps)
