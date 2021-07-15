def check_exam(correc,copie):
    return max(0, sum((not not reponse)*(5*(reponse==vrai)-1) for vrai,reponse in zip(correc,copie)))
  



