def countSetBits(n):
    count = 0
    while n:
        n = n & n - 1
        count = count + 1
    return count


def evil(n):
    return "It's Odious!" if countSetBits(n) % 2 == 1 else "It's Evil!"
