from string import ascii_lowercase

def solve(arr):
    print(arr)
    return [sum(1 for idx, _ in enumerate(word) if idx < 26 and word[idx].lower() == ascii_lowercase[idx]) for word in arr]
