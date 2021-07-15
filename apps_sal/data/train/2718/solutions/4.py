timed_reading=lambda m,t:len([e for e in __import__('re').findall('\w+',t)if len(e)<=m])
