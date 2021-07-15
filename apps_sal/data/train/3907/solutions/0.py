INSTRUCTIONS = {"0F12": int.__add__, "B7A2": int.__sub__, "C3D9": int.__mul__}

def communication_module(packet):
    header,inst,d1,d2,footer = (packet[i:i+4] for i in range(0,20,4))
    res = max(0, min(9999, INSTRUCTIONS[inst](int(d1), int(d2)) ))
    
    return f"{header}FFFF{res:0>4}0000{footer}"
