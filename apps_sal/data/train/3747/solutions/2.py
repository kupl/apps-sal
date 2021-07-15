def ipv4_address(address):
    return address.count(".")==3 and all([str.isdigit(s) and s==str(int(s)) and int(s)>=0 and int(s)<256 for s in address.split(".")])
