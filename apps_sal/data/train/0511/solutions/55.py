
def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    all = 0
    for ele in a:
        all ^= ele
    for ele in a:
        print(all ^ ele,end = " ")
    print()



def __starting_point():
    main()
__starting_point()
