def write_bar(new_bar, beat, amount):                                               
    new_beat = [str(int(fret) + amount) if fret.isnumeric() else fret for fret in beat]
    values = [int(fret) for fret in new_beat if fret.lstrip('-').isnumeric()]       
    if values and (max(values) > 22 or min(values) <= 0):                           
        raise ValueError('Out of frets!')                                           
    formatted_beat = [beat.ljust(len(max(new_beat, key=len)), '-') for beat in new_beat]
    for beat in range(len(formatted_beat)):                                         
        new_bar[beat] += formatted_beat[beat]                                       
    return new_bar                                                                  
                                                                                    
def transpose_bar(amount, bar):                                                     
    new_bar = [''] * 6                                                              
    frets = [''] * 6                                                                
    joined = False                                                                  
    for beat in range(len(bar[0])):                                                 
        if not joined:                                                              
            previous_beat = frets                                                   
        else:                                                                       
            previous_beat = [''] * 6                                                
        joined = False                                                              
        frets = [gen[beat] for gen in bar]                                          
        for fret in range(len(frets)):                                              
            if frets[fret].isnumeric() and previous_beat[fret].isnumeric():         
                previous_beat[fret] += frets[fret]                                  
                joined = True                                                       
        new_bar = write_bar(new_bar, previous_beat, amount)                         
                                                                                    
    if not joined:                                                                  
        new_bar = write_bar(new_bar, frets, amount)                                 
                                                                                    
    return new_bar                                                                  
                                                                                    
                                                                                    
def transpose(amount, tab):                                                         
    string_bars = [gen.split('|')[1:-1] for gen in tab]                             
    bars = list(zip(*string_bars))                                                  
    new_bars = [('e','B','G','D','A','E'),]                                         
    try:                                                                            
        for bar in bars:                                                            
            new_bars.append(transpose_bar(amount, bar))                             
        new_bars.append([''] * 6)                                                   
        transposed = list(zip(*new_bars))                                           
        return ['|'.join(gen) for gen in transposed]                                
    except ValueError as e:                                                         
        return str(e)   
