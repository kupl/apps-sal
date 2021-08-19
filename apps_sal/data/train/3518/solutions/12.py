def linux_type(file_attribute):
    types = {'-': 'file', 'd': 'directory', 'l': 'symlink', 'c': 'character_file', 'b': 'block_file', 'p': 'pipe', 's': 'socket', 'D': 'door'}
    if not file_attribute:
        return None
    ty = file_attribute[0]
    if ty in types:
        return types[ty]
    else:
        return None
