import re


def linux_type(file_attribute):
    types = {"-": "file",
             "d": "directory",
             "l": "symlink",
             "c": 'character_file',
             "b": 'block_file',
             "p": "pipe",
             "s": "socket",
             "D": "door"
             }
    return types[file_attribute[0]]
