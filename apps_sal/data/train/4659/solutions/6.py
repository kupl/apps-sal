def ip_to_int(s):
    return str(int("".join(f"{int(n):08b}" for n in s.split(".")), 2))


def int_to_ip(s):
    return ".".join(str(int(b, 2)) for b in (f"{int(s):032b}"[i:i + 8] for i in range(0, 32, 8)))


def numberAndIPaddress(s):
    return ip_to_int(s) if "." in s else int_to_ip(s)
