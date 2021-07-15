import re

def brainfuck_to_c(sc):
  code,p,l,t=[],0,-1,0
  while l!=len(sc): l=len(sc); sc=re.sub(r'(\+\-)|(\-\+)|(<>)|(><)|(\[\])|[^+\-<>,.\[\]]','',sc)
  l,braces=-1,re.sub(r'[+\-.<>,]','',sc)
  while l!=len(braces): l=len(braces); braces=re.sub(r'(\[\])','',braces)
  if len(braces)!=0: return "Error!"  
  while p<len(sc):
    c=sc[p]
    if c in '+-><':
      if   c=='+': m,v,o='+','*','+'
      elif c=='-': m,v,o='-','*','-'
      elif c=='>': m,v,o='>', '','+'
      elif c=='<': m,v,o='<', '','-'
      n=re.match('\\'+m+'+',sc[p:]).group(); p+=len(n)-1
      code.append(' '*t+v+'p '+o+'= '+str(len(n))+';')
    elif  c=='.': code.append(' '*t+'putchar(*p);')
    elif  c==',': code.append(' '*t+'*p = getchar();')
    elif  c=='[': code.append(' '*t+'if (*p) do {'); t+=2
    else: t-=2;   code.append(' '*t+'} while (*p);')
    p+=1
  return '' if sc=='' else '\n'.join(code)+'\n'
