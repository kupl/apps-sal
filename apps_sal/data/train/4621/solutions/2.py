import re

def count_deaf_rats(town):
    town = re.sub("(~O|O~)", lambda m: ">" if m.group(1) == "~O" else "<", town)
    left, right = town.split("P")
    return left.count("<") + right.count(">")
