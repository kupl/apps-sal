from ipaddress import ip_network
from typing import List, Union


def ipsubnet2list(subnet: str) -> Union[List[str], None]:
    try:
        return list(map(str, ip_network(subnet).hosts()))
    except ValueError:
        return
