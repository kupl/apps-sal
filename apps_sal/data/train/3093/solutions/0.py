import re


def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
