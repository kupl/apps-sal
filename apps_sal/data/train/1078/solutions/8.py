def solve(s, a, b, c):
    if s >= a + b + c:
        return 1
    if s >= a + b:
        return 2
    if s >= b + c:
        return 2
    return 3


def main():
    t = int(input())  # cook your dish here

    for _ in range(t):
        line = input().strip()
        s, a, b, c = [int(x) for x in line.split(" ")]
        print(solve(s, a, b, c))


main()
