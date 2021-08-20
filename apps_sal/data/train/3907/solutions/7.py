def communication_module(packet):
    (header, instruction, data1, data2, footer) = (packet[:4], packet[4:8], int(packet[8:12]), int(packet[12:16]), packet[-4:])
    operations = {'0F12': data1 + data2, 'B7A2': data1 - data2, 'C3D9': data1 * data2}
    calc_str = str(min(9999, max(0, operations[instruction]))).zfill(4)
    (instruction, data2R) = ('F' * 4, '0' * 4)
    return header + instruction + calc_str + data2R + footer
