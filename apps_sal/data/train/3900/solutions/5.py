s = '''|  
| 
| 
| 
|       |       |  
| 
| 
| 
|  
'''.splitlines()
def segment_display(n): return '\n'.join(''.join(i) + '|'for i in [(['|       '] * (6 - len(str(n)))) + [k[int(l)]for l in str(n)]for k in [[i[j:j + 8]for j in range(0, len(i), 8)]for i in s]])
