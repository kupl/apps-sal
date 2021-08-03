import re


def count_deaf_rats(town):
    return re.findall(r"O~|~O", town.split("P")[0]).count("O~") + re.findall(r"O~|~O", town.split("P")[1]).count("~O")
