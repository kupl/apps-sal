def ipToNum(ip):
    return str(int(''.join((f'{n:08b}' for n in map(int, ip.split('.')))), 2))


def numToIp(nums):
    b = f'{int(nums):032b}'
    return '.'.join(map(str, [int(b[i:i + 8], 2) for i in (0, 8, 16, 24)]))


def numberAndIPaddress(s):
    if '.' in s:
        return ipToNum(s)
    elif '.' not in s:
        return numToIp(s)
