def numberAndIPaddress(s):
    def ip2num(ip): return sum(el * (256 ** (4 - i)) for i, el in enumerate(map(int, ip.split('.')), 1))
    def num2ip(n): return '.'.join(map(str, [n >> 24, n >> 16 & 255, n >> 8 & 255, n & 255]))
    return str(ip2num(s)) if s.find('.') > 0 else num2ip(int(s))
