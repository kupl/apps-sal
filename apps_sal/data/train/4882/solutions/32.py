def round_to_next5(n):
    # Your code here
    # bool(n % 5) returns False if n is equally divisible, True if it isn't.
    # int(False) = 0; int(True) = 1
    return 5 * (n//5 + int(bool(n % 5)))
