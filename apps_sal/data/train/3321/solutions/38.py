def evil(n):
    evil_odious_count = str(bin(n).replace('0b', '')).count('1')
    return "It's Evil!" if evil_odious_count % 2 == 0 else "It's Odious!"
