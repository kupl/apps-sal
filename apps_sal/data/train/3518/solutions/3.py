def linux_type(file_attribute):
    flags = {
        '-': 'file',
        'd': 'directory',
        'l': 'symlink',
        'c': 'character_file',
        'b': 'block_file',
        'p': 'pipe',
        's': 'socket',
        'D': 'door'
    } 
    return flags[file_attribute[0]]
