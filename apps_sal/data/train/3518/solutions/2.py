D = {'p': 'pipe', '-': 'file', 'd': 'directory', 'l': 'symlink', 'c': 'character_file', 'b': 'block_file', 's': 'socket', 'D': 'door'}


def linux_type(file_attribute):
    return D[file_attribute[0]]
