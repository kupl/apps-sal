def parse(crontab):
    """
            "minute         1",
            "hour           2",
            "day of month   3",
            "month          4",
            "day of week    5",
    """
    
    fields = crontab.split()
    
    minutes = interpret_minutes(fields[0])
    hours = interpret_hours(fields[1])
    days_m = interpret_days_month(fields[2])
    months = interpret_months(fields[3])
    days_w = interpret_days_week(fields[4])
    
    result  = "minute         " + " ".join([str(v) for v in sorted(list(minutes))]) + "\n"
    result += "hour           " + " ".join([str(v) for v in sorted(list(hours))]) + "\n"
    result += "day of month   " + " ".join([str(v) for v in sorted(list(days_m))]) + "\n"
    result += "month          " + " ".join([str(v) for v in sorted(list(months))]) + "\n"
    result += "day of week    " + " ".join([str(v) for v in sorted(list(days_w))])
    
    return result
    
def interpret_minutes(cr_minutes):

    def interpret_minute(cr_field):            
        step = "1"   
        value = cr_field
        if cr_field.find('/') != -1:
            (value, step) = cr_field.split("/")
            
        low_min = 0
        hig_min = 59
        if value == "*":
            low_min = 0
            hig_min = 59
        elif value.find('-') != -1:
            (lm, hm) = value.split("-")
            low_min = int(lm)
            hig_min = int(hm)
        else:
            low_min = hig_min = int(value)
            
        return set(range(low_min, hig_min+1, int(step)))
        
    result_set = set()
    for request in cr_minutes.split(","):
        new_set = interpret_minute(request)
        result_set.update(new_set)
        
    return result_set   
        

def interpret_hours(cr_hours):
    def interpret_hour(cr_field):            
        step = "1"   
        value = cr_field
        if cr_field.find('/') != -1:
            (value, step) = cr_field.split("/")
            
        low_min = 0
        hig_min = 23
        if value == "*":
            low_min = 0
            hig_min = 23
        elif value.find('-') != -1:
            (lm, hm) = value.split("-")
            low_min = int(lm)
            hig_min = int(hm)
        else:
            low_min = hig_min = int(value)
            
        return set(range(low_min, hig_min+1, int(step)))
    
    result_set = set()
    for request in cr_hours.split(","):
        new_set = interpret_hour(request)
        result_set.update(new_set)
        
    return result_set   


def interpret_days_month(cr_days_m):
    def interpret_day_month(cr_field):            
        step = "1"   
        value = cr_field
        if cr_field.find('/') != -1:
            (value, step) = cr_field.split("/")
            
        low_min = 1
        hig_min = 31
        if value == "*":
            low_min = 1
            hig_min = 31
        elif value.find('-') != -1:
            (lm, hm) = value.split("-")
            low_min = int(lm)
            hig_min = int(hm)
        else:
            low_min = hig_min = int(value)
            
        return set(range(low_min, hig_min+1, int(step)))
    
    result_set = set()
    for request in cr_days_m.split(","):
        new_set = interpret_day_month(request)
        result_set.update(new_set)
        
    return result_set   

    
def interpret_months(cr_months):
    def interpret_month(cr_field):
        names_to_numbers = {
            'JAN': "1", 'FEB': "2", 'MAR': "3", 'APR': "4", 'MAY': "5",
            'JUN': "6", 'JUL': "7", 'AUG': "8", 'SEP': "9", 'OCT': "10",
            'NOV': "11", 'DEC': "12"
        }
        
        step = "1"   
        value = cr_field
        if cr_field.find('/') != -1:
            (value, step) = cr_field.split("/")
            
        low_min = 1
        hig_min = 12
        if value == "*":
            low_min = 1
            hig_min = 12
        elif value.find('-') != -1:
            (lm, hm) = value.split("-")
            low_min = int(names_to_numbers.get(lm, lm))
            hig_min = int(names_to_numbers.get(hm, hm))
        else:
            low_min = hig_min = int(names_to_numbers.get(value, value))
            
        return set(range(low_min, hig_min+1, int(step)))
    
    result_set = set()
    for request in cr_months.split(","):
        new_set = interpret_month(request)
        result_set.update(new_set)
        
    return result_set   

def interpret_days_week(cr_days_w):
    def interpret_day_week(cr_field):
        names_to_numbers = {
            'SUN': "0", 'MON': "1", 'TUE': "2", 'WED': "3",
            'THU': "4", 'FRI': "5", 'SAT': "6"
        }
        
        step = "1"   
        value = cr_field
        if cr_field.find('/') != -1:
            (value, step) = cr_field.split("/")
            
        low_min = 0
        hig_min = 6
        if value == "*":
            low_min = 0
            hig_min = 6
        elif value.find('-') != -1:
            (lm, hm) = value.split("-")
            low_min = int(names_to_numbers.get(lm, lm))
            hig_min = int(names_to_numbers.get(hm, hm))
        else:
            low_min = hig_min = int(names_to_numbers.get(value, value))
            
        return set(range(low_min, hig_min+1, int(step)))
    
    result_set = set()
    for request in cr_days_w.split(","):
        new_set = interpret_day_week(request)
        result_set.update(new_set)
        
    return result_set   

