RULES = {1: lambda x: ''.join(x[0][:4]).upper(), 2: lambda x: ''.join(x[0][:2] + x[1][:2]).upper(), 3: lambda x: ''.join(x[0][:1] + x[1][:1] + x[2][:2]).upper(), 4: lambda x: ''.join(x[0][:1] + x[1][:1] + x[2][:1] + x[3][:1]).upper()}


def bird_code(arr):
    arr = [bird.replace('-', ' ') for bird in arr]
    ret_arr = []
    for bird in arr:
        name_parts = bird.split()
        ret_arr.append(RULES[len(name_parts)](name_parts))
    return ret_arr
