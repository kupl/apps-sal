solve=lambda Q,S:not __import__('re').sub(Q.replace('*','.*'),'',S)
