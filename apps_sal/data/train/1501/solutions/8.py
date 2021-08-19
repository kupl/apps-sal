def main():
    (n, q) = list(map(int, input().split()))
    edges = (pow(2, n, 1000000007) - 1) * 2 % 1000000007
    bottom = pow(2, n, 1000000007)
    top = 1
    right = n + 1
    left = n + 1
    for i in range(q):
        query = list(map(int, input().split()))
        if len(query) == 1:
            print(edges)
        else:
            op = query[1]
            if op == 1:
                edges *= 2
                edges += right
                edges = edges % 1000000007
                bottom *= 2
                top *= 2
            elif op == 2:
                edges *= 2
                edges += left
                edges = edges % 1000000007
                bottom *= 2
                top *= 2
            elif op == 3:
                edges *= 2
                edges += top
                edges = edges % 1000000007
                left *= 2
                right *= 2
                top = bottom
            else:
                edges *= 2
                edges += bottom
                edges = edges % 1000000007
                left *= 2
                right *= 2
                bottom = top
            left = left % 1000000007
            right = right % 1000000007
            bottom = bottom % 1000000007
            top = top % 1000000007


main()
