def bucket_of(said):
    teststring = said.lower()
    result = []
    water = ['water', 'wet', 'wash']
    slime = ["i don't know", 'slime']
    for i in range(len(water)):
        if water[i] in teststring:
            result.append('water')
        else:
            continue
    for i in range(len(slime)):
        if slime[i] in teststring:
            result.append('slime')
        else:
            continue
    if 'water' in result and 'slime' in result:
        return 'sludge'
    elif 'water' in result:
        return 'water'
    elif 'slime' in result:
        return 'slime'
    else:
        return 'air'
