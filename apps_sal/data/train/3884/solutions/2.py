import re

def gym_slang(phrase, *args):
    def repl_f (repl):
        def g (match):
            return repl.capitalize () if match.group (0) [0].isupper () else repl
        return g
        
    r = phrase
    r = re.sub ('(p|P)robably', repl_f ('prolly'), r)
    r = re.sub ('(i|I) am', repl_f ('i\'m'), r)
    r = re.sub ('(i|I)nstagram', repl_f ('insta'), r)
    r = re.sub ('(d|D)o not', repl_f ('don\'t'), r)
    r = re.sub ('(g|G)oing to', repl_f ('gonna'), r)
    r = re.sub ('(c|C)ombination', repl_f ('combo'), r)
    return r

