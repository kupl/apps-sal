
def __starting_point():
    N = int(input().strip())
    stamps = set()

    for _ in range(N):
        stamp = input().strip()
        stamps.add(stamp)

    print(len(stamps))


__starting_point()
