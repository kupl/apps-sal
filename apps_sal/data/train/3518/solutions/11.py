def linux_type(file_attribute):
    return {'d': 'directory', 'l': 'symlink', 'c': 'character_file', 'b': 'block_file', 'p': 'pipe', 's': 'socket', 'D': 'door'}.get(file_attribute[0], 'file')
