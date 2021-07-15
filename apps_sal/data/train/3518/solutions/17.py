def linux_type(file_attribute):
    f_att = file_attribute[0]
    if f_att == '-':
        return "file"
    elif f_att == 'd':
        return "directory"
    elif f_att == 'l':
        return "symlink"
    elif f_att == 'c':
        return "character_file"
    elif f_att == 'b':
        return "block_file"
    elif f_att == 'p':
        return "pipe"
    elif f_att == 's':
        return "socket"
    elif f_att == 'D':
        return "door"
    return None
