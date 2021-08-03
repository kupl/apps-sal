def case_sensitive(s):
    result = [char for char in s if char.isupper()]
    return [result == [], result]
