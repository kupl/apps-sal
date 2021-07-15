# cook your dish here
def __starting_point():
    for _ in range(int(input())):
        b, g = map(int, input().split())
        print(2*(g+b-1))
__starting_point()
