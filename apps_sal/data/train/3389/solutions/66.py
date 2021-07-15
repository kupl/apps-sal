import re

domain_name = lambda url: re.search(r"^(https?\:\/\/)?(www.)?([a-zA-Z0-9\-]+)", url).group(3)
