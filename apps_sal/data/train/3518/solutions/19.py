def linux_type(file_attribute):
    Unix_system_type = [['-', 'file'], ['d', 'directory'], ['l', 'symlink'], ['c', 'character_file'], ['b', 'block_file'], ['p', 'pipe'], ['s', 'socket'], ['D', 'door']]
    i = 0
    while i < len(Unix_system_type):
        if file_attribute[0] == Unix_system_type[i][0]:
            return Unix_system_type[i][1]
        i += 1
