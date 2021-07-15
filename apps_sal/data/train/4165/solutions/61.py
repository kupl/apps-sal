def uni_total(string):
    #your code here
    try: 
        return sum([ord(i) for i in string])
    except:
        return 0
