ant_bridge=lambda w,s:(lambda n:w[n:]+w[:n])(-len(''.join(__import__('re').findall('(?:-\.+)+-',s)))%len(w))
