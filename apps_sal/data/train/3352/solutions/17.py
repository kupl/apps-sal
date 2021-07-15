# Negative available

def find_longest(arr):
    return max(arr, key=lambda x: int(__import__('math').log10(abs(x))))

# def find_longest(arr):
#     return max(arr, key=lambda x: len(str(abs(x))))

