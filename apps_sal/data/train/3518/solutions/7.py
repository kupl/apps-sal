def linux_type(f):
    return {'-':'file','d':'directory','l':'symlink','c':'character_file','b':'block_file','p':'pipe','s':'socket','D':'door'}.get(f[0])

