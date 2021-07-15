from typing import List, Union
def digit_sum(n: Union[List[int], int]) -> int:
    """
    Finds the digit sum of the digits in an integer or list of positional integers
    """
    if isinstance(n, list):
        return sum(n)        
    return sum(int(ch) for ch in str(n))

def to_int(arr: List[int]) -> int:
    """
    Converts an array of positional integers into a single integer
    """
    return int(''.join(str(n) for n in arr))

def bump(arr, i):
    """
    Takes the digits of an array and increments the digit at index i and decrements the digit at 
    index i + 1.
    E.g. bump([1, 2, 8, 4], 1) -> [1, 2+1, 8-1, 4] -> [1, 3, 7, 4]
    """
    return arr[:i] + [arr[i] + 1] + [arr[i + 1] - 1] + arr[i+2:]

def solve(n: int) -> int:
    """
    Find the largest number <= n with the maximum digit sum
    """
    s = str(n)
    # Decrement the first digit and convert all others to 9 as a baseline
    option = [int(s[0]) - 1] + [9] * (len(s) - 1)
    if digit_sum(option) > digit_sum(n):
        for i in range(len(option) - 1):
            # Keep bumping digit i in option while still a single digit and the int value <= n
            while True:
                if option[i] == 9:
                    break
                b = bump(option, i)
                if to_int(b) > n:
                    break
                option = b
        return to_int(option)
    return n
