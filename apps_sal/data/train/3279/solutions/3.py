sursurungal=lambda s:__import__('re').sub(r'(\d+) (\w+)',lambda x:(lambda a,b:str(a)+' '+[[['bu'+b[:-1],b[:-1]+'zo'][a>2],'ga'+b[:-1]+'ga'][a>9],b][a<2])(int(x.group(1)),x.group(2)),s)
