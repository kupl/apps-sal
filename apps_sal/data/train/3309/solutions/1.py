COLORS = {'0': 'black', '1': 'brown', '2': 'red', '3': 'orange', '4': 'yellow', '5': 'green', '6': 'blue', '7': 'violet', '8': 'gray', '9': 'white'}

def encode_resistor_colors(ohmS):
    ohmS = str(int(eval(ohmS.replace(' ohms','').replace('k','*1000').replace('M','*1000000'))))
    return "{} {} {} gold".format(COLORS[ohmS[0]], COLORS[ohmS[1]], COLORS[ str(len(ohmS[2:])) ] )
