def solution(string):
    len_str = len(string)
    reverse = []
    while len_str > 0:
        reverse += string[len_str - 1]
        len_str -= 1
    reverse_str = "".join(reverse)
    return reverse_str
