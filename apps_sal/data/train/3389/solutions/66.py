import re


def domain_name(url): return re.search(r"^(https?\:\/\/)?(www.)?([a-zA-Z0-9\-]+)", url).group(3)
