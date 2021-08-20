def main():
    while True:
        h = int(input())
        if h == 0:
            break
        lineproc = input().split()
        nodes = []
        nodes.append(int(lineproc[0]))
        for i in range(1, int(2 ** h) - 1):
            number = int(lineproc[i]) * nodes[int((i + 1) / 2) - 1]
            nodes.append(number)
        print(max(nodes) % 1000000007)


main()
