def evil(n):
    return "It's Evil!" if (sum([i == '1' for i in str(bin(n))]) % 2 == 0) else "It's Odious!"
