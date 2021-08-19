def encrypter(s):
    return ''.join(['mlkjihgfedcbazyxwvutsrqpon'['abcdefghijklmnopqrstuvwxyz'.index(a)] if a in 'abcdefghijklmnopqrstuvwxyz' else a for a in s])
