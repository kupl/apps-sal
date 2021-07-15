list_with_keys = list(map(chr,range(ord('a'),ord('f')+1)))

my_list = []
for item in list(range(10)):
    my_list.append(str(item))
    
list_with_keys = my_list + list_with_keys
list_with_values = list(range(16))

hex_dict = dict(zip(list_with_keys,list_with_values))

def hex_to_dec(s):
    hex_convert = []
    for char in list(s):
        for key, value in hex_dict.items():
            if char == key: hex_convert.append(value)
    hex_num = 0
    for (index,number) in zip(range(len(hex_convert)),reversed(hex_convert)):
        hex_num = hex_num + (number*(16**index))
    return hex_num
