def protein_synthesis(dna):
  r = dna.translate(str.maketrans('TACG','AUGC'))
  r = list(r[i:i+3] for i in range(0,len(r),3))
  return (' '.join(r), ' '.join([CODON_DICT[i] if len(i)>2 else '' for i in r]).strip())
