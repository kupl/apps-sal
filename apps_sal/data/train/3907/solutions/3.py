def communication_module(packet):
    header, footer = packet[:4], packet[-4:]
    instr, rvalue = packet[4:8], 'FFFF'
    data1, data2 = packet[8:12], packet[12:16]
    
    if instr == '0F12':
        calc = int(data1) + int(data2)
    elif instr == 'B7A2':
        calc = int(data1) - int(data2)
    elif instr == 'C3D9':
        calc = int(data1) * int(data2)
        
    if calc > 9999:
        calc = 9999
    elif calc < 0:
        calc = 0
        
    rstring = f'{header}{rvalue}{calc:04d}0000{footer}'
    
    return rstring
