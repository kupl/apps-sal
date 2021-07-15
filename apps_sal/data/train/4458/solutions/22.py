def time_correct(t):
    
    try:
        if t == None:
            return None
        
        if t == "":
            return ""
        
        if len(t) < 8:
            return None
        
        for char in t:
            if not (char.isdigit() or char == ':'):
                return None
            
        # get numerical values from string
        times = t.split(':')
        hours = int(times[0])
        minutes = int(times[1])
        seconds = int(times[2])
        
        # correct values
        minutes += seconds // 60        
        seconds = seconds % 60
        hours += minutes // 60       
        minutes = minutes % 60
        hours = hours % 24
        
        #process values into string format
        hours = str(hours) if len(str(hours))==2 else ('0' + str(hours))
        minutes = str(minutes) if len(str(minutes))==2 else ('0' + str(minutes))
        seconds = str(seconds) if len(str(seconds))==2 else ('0' + str(seconds))
        
        return f"{hours}:{minutes}:{seconds}"

    except:
        return None

