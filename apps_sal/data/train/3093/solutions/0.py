import re


def insert_dash(num):
    # your code here
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
