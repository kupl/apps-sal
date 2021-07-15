sea_sick = lambda s: ['No Problem','Throw Up'][sum(__import__("itertools").starmap(str.__ne__, zip(s, s[1:]))) / len(s) > 0.2]
