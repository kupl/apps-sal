def modes(data):
    frequency = {}
    mode_list = []
    
    # adds or creates a counter for each character
    for d in data:
        if d in frequency:
            frequency[d] += 1
        else:
            frequency[d] = 1
    
    # adds modes from the dictionary to a list, and checks that there is a mode
    for f in frequency:
        if frequency[f] == max(frequency.values()) > min(frequency.values()):
            mode_list.append(f)
            
    return sorted(mode_list)
