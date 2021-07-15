def dna_to_rna(dna):
  t= ''
  for x in dna:
    if(x=='T'):
      x='U'
    t+=x  
    #print(t)
  return(t)


