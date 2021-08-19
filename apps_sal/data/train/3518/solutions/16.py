D = {'-': 'file', 'd': 'directory', 'l': 'symlink', 'c': 'character_file', 'b': 'block_file', 'p': 'pipe', 's': 'socket', 'D': 'door'}


def linux_type(s):
    return D[s[0]]
