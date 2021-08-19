def unlock(message):
    return ''.join(('8' if i == 'v' else '7' if i == 's' else str(2 + min(7, (ord(i) - ord('a')) // 3)) for i in message.lower()))
