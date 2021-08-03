def travel(r: str, zipcode: str) -> str:
    addresses, numbers = [], []
    if zipcode:
        for a in r.split(','):
            s, _, rem = a.rpartition(zipcode)
            if s and not rem:
                n, a = s[:-1].split(maxsplit=1)
                numbers.append(n)
                addresses.append(a)

    return f"{zipcode}:{','.join(addresses)}/{','.join(numbers)}"
