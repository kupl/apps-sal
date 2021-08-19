def cidr_to_bits(subnet):
    subnet_int = int(subnet[-2:])
    mask_in_bits = [(1, 0)[i > subnet_int] for i in range(1, 33)]
    return mask_in_bits


def ip_bits(subnet):
    ip_bits_str = list([format(int(x), '#010b')[2:] for x in subnet[:-3].split('.')])
    ip_bits_int = [int(i) for x in ip_bits_str for i in x]
    return ip_bits_int


def f_addr_bits(x):
    return [i & j for (i, j) in zip(ip_bits(x), cidr_to_bits(x))]


def l_addr_bits(x):
    not_on_mask = [(0, 1)[i == 0] for i in cidr_to_bits(x)]
    return [i | j for (i, j) in zip(f_addr_bits(x), not_on_mask)]


def address_to_int(bits_lst):
    return [int(''.join((str(bits_lst[y + i]) for i in range(8))), 2) for y in range(0, 32, 8)]


def list_of_addresses(x):
    first_address = address_to_int(f_addr_bits(x))
    last_address = address_to_int(l_addr_bits(x))
    octets_ranges = [[i for i in range(i, j + 1)] if j - i != 0 else [i] for (i, j) in zip(first_address, last_address)]
    addresses = []
    for first_oct in octets_ranges[0]:
        for second in octets_ranges[1]:
            for third in octets_ranges[2]:
                for fourth in octets_ranges[3]:
                    addresses.append(f'{first_oct}.{second}.{third}.{fourth}')
    return addresses


def ipsubnet2list(subnet):
    result = list_of_addresses(subnet)
    if subnet[:-3] in result:
        if len(result) == 2:
            return result
        return result[1:-1]
    else:
        return None
