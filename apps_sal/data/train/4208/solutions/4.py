from ipaddress import ip_network


def ipsubnet2list(subnet):
    try:
        return [ip.compressed for ip in ip_network(subnet).hosts()]
    except ValueError:
        return
