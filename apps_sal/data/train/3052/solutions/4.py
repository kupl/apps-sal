def remove(string):
    return string.replace('!', '') + '!'*(len(string)- len(string.rstrip('!')))
