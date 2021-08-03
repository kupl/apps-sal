import re


def ipv4_address(address):
    return (
        bool(re.match(r'\d+(\.\d+){3}\Z', address)) and
        all(0 <= int(x) <= 255 and (x == '0' or not x.startswith('0')) for x in re.findall(r'\d+', address))
    )
