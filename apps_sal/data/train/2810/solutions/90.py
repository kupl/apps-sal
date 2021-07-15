from string import ascii_lowercase as lower_alpha
def solve(arr):
    return [sum(char == lower_alpha[i] for i,char in enumerate(word[:26].lower())) for word in arr]
