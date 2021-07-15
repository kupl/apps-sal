import re
def decipher_this(text):
    return re.sub(r'\b(\d{2,3})(\w?)(\w*?)(\w?)\b', lambda m: '{}'.format(chr(int(m.group(1))) + m.group(4) + m.group(3) + m.group(2)), text)
