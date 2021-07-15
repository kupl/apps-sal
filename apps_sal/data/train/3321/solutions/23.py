def evil(n: int) -> str:
    """
    Check if the given number is:
     - evil: it has an even number of 1's in its binary representation
     - odious: it has an odd number of 1's in its binary representation
    """
    return f"It's {'Odious' if str(bin(n)).count('1') % 2 else 'Evil'}!"
