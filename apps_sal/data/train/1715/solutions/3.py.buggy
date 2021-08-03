  def justify(text, width):
      output = ""
      while len(text) > width:
          line = text[0:width]
          if text[width] == ' ': # Ideal case, cut on space, no need to justify anything
              output += line + '\n' 
              text = text[width+1:]
              continue
          line = line[0:line.rfind(' ')] # Remove the impartial word from the end of line
          text = text[len(line)+1:]
          words = line.split(" ")
          if len(words) > 1:
          # If there are more than one word, add missing spacing by adding one space
          # to each word except last one and repeat until there is no more missing spacing left.
              for x in xrange(0,width - len(line)):
                  words[x % (len(words)-1)] += ' '
          output += " ".join(words) + '\n'
      return output + text

