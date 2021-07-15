
def likes(names):
    output = {
        0 : "no one likes this",
        1 : "{} likes this",
        2 : "{} and {} like this",
        3 : "{}, {} and {} like this",
        4 : "{}, {} and {others} others like this",
    }
    
    count = len(names)
    
    return output[min(4,count)].format(*names[:3], others=count-2)
