def prime_maxlength_chain(val_max):
   
    # Calcula os primos usando o crivo
    primes = []
    sieve = [1]*(val_max+1)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, (val_max+1)):
        if sieve[i] == 0:
            continue
        for j in range(i*i, (val_max+1), i):
            sieve[j] = 0
           
    # Guarda os primos num array separado
    for i in range(val_max+1):
      if sieve[i] == 1:
        primes.append(i)
   
    # Testa encontrar primos que são somas de 'j' primos consecutivos    
    for j in range (400, -1, -1):
     
      # Aplica uma tecnica de janela deslizante (adicionando um cara na frente e removendo o do fundo) pra calcular mais rapido todas as janelas possiveis
      answer = []
      acc = 0
      if len(primes) < j:
        continue
     
      # Coloca os primeiros caras na janela atual
      for i in range(j):
        acc += primes[i]
     
      # Testa se eh primo
      if acc <= val_max and sieve[acc] == 1:
        answer.append(acc)
     
      # Aqui faz o procedimento de colocar o proximo cara e tirar o ultimo da janela ('deslizando' a janela pra frente)
      for i in range(j, len(primes)):
        acc += primes[i]
        acc -= primes[i-j]
        # Quando o valor ja for maior que o maximo, já pode parar
        if acc >= val_max:
          break
        # Verifica se eh primo
        if acc <= val_max and sieve[acc] == 1:
          answer.append(acc)
      # Se com o tamanho 'j' a gente encontrou resposta, a resposta eh a lista de primos com esse tamanho
      if len(answer) > 0:
        return answer

