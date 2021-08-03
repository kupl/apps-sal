# checks if string a or b is longer
# returns string short_string+long_string+short_string
def solution(a, b):
    return a + b + a if len(a) <= len(b) else b + a + b
