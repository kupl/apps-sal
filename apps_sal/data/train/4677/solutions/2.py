import hashlib
def create_crack(n):
    rainbow = {hashlib.md5(f'{a:05}'.encode()).hexdigest() : f'{a:05}' for a in range(10 ** n)}
    return rainbow.get

crack = create_crack(6)

