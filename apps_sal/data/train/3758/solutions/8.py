import re


def word_mesh(arr):
    mesh = re.findall('(.+)-(?=\\1)', '-'.join(arr))
    return ''.join(mesh) if len(mesh) == len(arr) - 1 else 'failed to mesh'
