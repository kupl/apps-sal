import re


def word_mesh(arr):
    common = re.findall('(.+) (?=\\1)', ' '.join(arr))
    return ''.join(common) if len(common) + 1 == len(arr) else 'failed to mesh'
