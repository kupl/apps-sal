def hotpo(num, count=0):
    return count if num == 1 else hotpo(num / 2 if num % 2 == 0 else num * 3 + 1, count + 1)
