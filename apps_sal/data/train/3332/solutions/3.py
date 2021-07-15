import re
def autocorrect(input):
    return re.sub(r"\b(yo[u]+|[u])(?!'\w)\b",'your sister',input,flags=re.IGNORECASE)
    
            
            

