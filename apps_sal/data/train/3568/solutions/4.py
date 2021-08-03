import re


def bumps(road):
    return "Woohoo!" if len(re.findall("n", road)) < 16 else "Car Dead"
