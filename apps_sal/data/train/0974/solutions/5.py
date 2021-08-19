# cook your dish here
def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = list(map(int, input().split()))
        if a == b:
            print("YES")
            continue
        if (a != b and c == d):
            print("NO")
            continue
        if(abs(b - a) % (max(c, d) - min(c, d)) == 0):
            print("YES")
        else:
            print("NO")


main()
