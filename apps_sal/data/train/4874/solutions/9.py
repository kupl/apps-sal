import re


def travel(r, zipcode):
    addresses = [*[x for x in r.split(",") if re.findall(r"[A-Z]{2} \d{5}", x)[0] == zipcode]]
    if not addresses:
        return f"{zipcode}:/"
    numbers = []
    for i, a in enumerate(addresses):
        n = re.findall(r"\d{1,5}(?= \w+)", a)[0]
        numbers.append(n)
        addresses[i] = a.strip(n).strip(zipcode)
    return f"{zipcode}:{','.join(addresses)}/{','.join(numbers)}"
