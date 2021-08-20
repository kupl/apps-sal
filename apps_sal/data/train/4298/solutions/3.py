def n00bify(text):
    import re
    replaced = re.sub('too|to|Too|To', '2', text)
    replaced = re.sub('fore|for|Fore|For|FORE', '4', replaced)
    replaced = re.sub('oo|Oo', '00', replaced)
    replaced = re.sub('be|Be', 'b', replaced)
    replaced = re.sub('are|Are', 'r', replaced)
    replaced = re.sub('you|You', 'u', replaced)
    replaced = re.sub('please|Please', 'plz', replaced)
    replaced = re.sub('people|People', 'ppl', replaced)
    replaced = re.sub('really|Really', 'rly', replaced)
    replaced = re.sub('have|Have', 'haz', replaced)
    replaced = re.sub('know|Know', 'no', replaced)
    replaced = re.sub('s', 'z', replaced)
    replaced = re.sub('S', 'Z', replaced)
    replaced = re.sub("[.,']", '', replaced)
    if text[0] in ['W', 'w']:
        if len(replaced.replace('!', '')) >= 28:
            replaced = 'LOL OMG ' + replaced
        else:
            replaced = 'LOL ' + replaced
    elif len(replaced.replace('!', '')) >= 32:
        replaced = 'OMG ' + replaced
    if text[0] in ['H', 'h']:
        replaced = replaced.upper()
    replaced = ' '.join([val.upper() if (i + 1) % 2 == 0 else val for (i, val) in enumerate(replaced.split())])
    num = len(replaced.split())
    replaced = replaced.replace('?', '?' * num)
    s = ''.join(['!' if i % 2 == 0 else '1' for i in range(num)])
    replaced = replaced.replace('!', s)
    return replaced
