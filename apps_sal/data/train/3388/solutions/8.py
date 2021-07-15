import re

def binary_to_string(binary):
    return re.sub(r'.'*8, lambda e: chr(int(e.group(), 2)), binary)
