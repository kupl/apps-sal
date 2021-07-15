def check_DNA(seq1, seq2):
 if len(seq1) < len(seq2): seq1, seq2 = seq2, seq1
 seq2 = seq2[::-1].replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()
 return seq1.find(seq2) >= 0
