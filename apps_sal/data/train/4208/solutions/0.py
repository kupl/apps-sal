import ipaddress as ip

def ipsubnet2list(subnet):
    try: return list(map(str,ip.ip_network(subnet).hosts()))
    except: pass
