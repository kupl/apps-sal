files_types = {'-': 'file',
               'd': 'directory',
               'l': 'symlink',
               'c': 'character_file',
               'b': 'block_file',
               'p': 'pipe',
               's': 'socket',
               'D': 'door'}


def linux_type(file_attribute):
    return files_types[file_attribute[0]]
