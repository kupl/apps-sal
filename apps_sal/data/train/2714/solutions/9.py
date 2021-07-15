def bucket_of(said):
    s = said.lower()
    
    if "slime" in s and "water" not in s:
        return "slime"
    
    elif "i don't know" in s:
        if "water" in s:
            return "sludge"
        return "slime"
    
    elif "water" in s or "wet" in s or "wash" in s:
        if "slime" in s:
            return "sludge"
        if "i don't know" in s:
            return "slime"
        return "water"
               
    return "air"          

