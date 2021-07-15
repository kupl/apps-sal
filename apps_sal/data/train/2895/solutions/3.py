def ka_co_ka_de_ka_me(word, tete='ka'):
    for i in range(len(word) - 1):
      tete+=word[i]        
      if word[i] in 'aeiouAEIOU':
        if word[i+1] not in 'aeiouAEIOU':
          tete+='ka';

    return tete + word[-1]
