import re, math

def convert_recipe(recipe):
    
    def repl(m):
        ratio = 15 if m.group(2) == "tbsp" else 5
        return m.group(0) + " (%sg)" % math.ceil(eval(m.group(1)) * ratio)
    
    return re.sub("([0-9/]+) (tb?sp)", repl, recipe)
