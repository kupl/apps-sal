def round_to_next5(n):
    # Your code here
    if n % 5 == 0:
        return n
    elif n % 5 != 0:
        while (n % 5) != 0:
            n = n + 1
            if (n % 5) == 0:
                return n 
                break
print(round_to_next5(30))
