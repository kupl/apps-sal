d = dict(__import__("re").findall(r"'(.)'.*\s([a-z_]+)\.",
                                  """
        '-' A regular file ==> file.
        'd' A directory ==> directory.
        'l' A symbolic link ==> symlink.
        'c' A character special file. It refers to a device that handles data as a stream of bytes (e.g: a terminal/modem) ==> character_file.
        'b' A block special file. It refers to a device that handles data in blocks (e.g: such as a hard drive or CD-ROM drive) ==> block_file.
        'p' a named pipe ==> pipe.
        's' a socket ==> socket.
        'D' a door ==> door.
    """))


def linux_type(s): return d[s[0]]
