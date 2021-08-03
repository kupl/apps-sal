from re import compile

r = compile("[aeiou]+")


def solve(s: str):
    return max(list(map(len, r.findall(s))))
