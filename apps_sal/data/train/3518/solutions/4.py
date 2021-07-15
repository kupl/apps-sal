def linux_type(file_attribute):
    switch = {
        '-': 'file',
        'd': 'directory',
        'l': 'symlink',
        'c': 'character_file',
        'b': 'block_file',
        'p': 'pipe',
        's': 'socket',
        'D': 'door',
    }
    return switch[file_attribute[0]]
