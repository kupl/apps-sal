def convert_num(n, base):
    return ("Invalid number input" if not isinstance(n, int)
            else "Invalid base input" if base not in ["bin", "hex"]
            else bin(n) if base == "bin"
            else hex(n))             # if base == "hex"
