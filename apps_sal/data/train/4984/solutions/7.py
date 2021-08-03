from functools import reduce


def meeting(s):
    people = [i.split(":")[::-1] for i in s.upper().split(";")]
    people.sort(key=lambda x: x[0] + " " + x[1])
    return reduce(lambda acc, x: acc + "(" + x[0] + ", " + x[1] + ")", people, "")
