
def n00bify(text):
    import re

    replaced = re.sub(r'too|to|Too|To', '2', text)
    replaced = re.sub(r'fore|for|Fore|For|FORE', '4', replaced)
    replaced = re.sub(r'oo|Oo', '00', replaced)
    replaced = re.sub(r'be|Be', 'b', replaced)
    replaced = re.sub(r'are|Are', 'r', replaced)
    replaced = re.sub(r'you|You', 'u', replaced)
    replaced = re.sub(r'please|Please', 'plz', replaced)
    replaced = re.sub(r'people|People', 'ppl', replaced)
    replaced = re.sub(r'really|Really', 'rly', replaced)
    replaced = re.sub(r'have|Have', 'haz', replaced)
    replaced = re.sub(r'know|Know', 'no', replaced)
    replaced = re.sub(r's', 'z', replaced)
    replaced = re.sub(r'S', 'Z', replaced)
    replaced = re.sub(r"[.,']", '', replaced)
    if text[0] in ['W', 'w']:
        if len(replaced.replace('!', '')) >= 28:
            replaced = 'LOL OMG ' + replaced
        else:
            replaced = 'LOL ' + replaced
    else:
        if len(replaced.replace('!', '')) >= 32:
            replaced = 'OMG ' + replaced
    if text[0] in ['H', 'h']:
        replaced = replaced.upper()
    replaced = ' '.join([val.upper() if (i + 1) % 2 == 0 else val for i, val in enumerate(replaced.split())])
    num = len(replaced.split())
    replaced = replaced.replace('?', '?' * num)
    s = ''.join(['!' if i % 2 == 0 else '1' for i in range(num)])
    replaced = replaced.replace('!', s)
    return replaced
