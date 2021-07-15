def linux_type(fa):
    d = {'-':'file',
          'd':'directory',
           'l':'symlink',
            'c': 'character_file',
            'b':'block_file',
            'p':'pipe',
            's':'socket',
            'D':'door'
         }
    return d.get(fa[0])
