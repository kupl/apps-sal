d = dict(__import__('re').findall("'(.)'.*\\s([a-z_]+)\\.", "\n        '-' A regular file ==> file.\n        'd' A directory ==> directory.\n        'l' A symbolic link ==> symlink.\n        'c' A character special file. It refers to a device that handles data as a stream of bytes (e.g: a terminal/modem) ==> character_file.\n        'b' A block special file. It refers to a device that handles data in blocks (e.g: such as a hard drive or CD-ROM drive) ==> block_file.\n        'p' a named pipe ==> pipe.\n        's' a socket ==> socket.\n        'D' a door ==> door.\n    "))


def linux_type(s):
    return d[s[0]]
