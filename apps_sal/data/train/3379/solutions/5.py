encrypter=lambda s: "".join(["mlkjihgfedcbazyxwvutsrqpon"["abcdefghijklmnopqrstuvwxyz".index(a)] if a in "abcdefghijklmnopqrstuvwxyz" else a for a in s])
