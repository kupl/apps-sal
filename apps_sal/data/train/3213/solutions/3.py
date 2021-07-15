import re

def sum_of_a_beach(beach):
    return sum(1 for _ in re.finditer(r'sand|water|fish|sun',beach.lower()))
