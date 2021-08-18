def main():
    n = int(input())
    numbers = list(map(int, input().split(" ")))
    numbers.sort()
    r = [numbers[n - 1 + x] - numbers[x] for x in range(n + 1)]
    print(min([r[0] * r[-1], (numbers[-1] - numbers[0]) * min(r)]))


main()
