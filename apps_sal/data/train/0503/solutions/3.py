class Solution:
    def arrangeWords(self, text: str) -> str:
        counter = 0
        current_word = ''
        words_map = {}
        for i in range(0, len(text)):
            ch = text[i].lower()
            if ch == ' ' or i == len(text) - 1:
                if i == len(text)-1:
                    counter += 1
                    current_word += ch
                    
                if counter not in words_map:
                    words_map[counter] = []
                    
                words_map[counter].append(current_word)
                
                counter = 0
                current_word = ''
            else:
                counter += 1
                current_word += ch
        
        ordered_keys = list(words_map.keys())
        ordered_keys.sort()
        
        ans = ''
        for i in range(0, len(ordered_keys)):
            if i == 0:
                ans = ' '.join(words_map[ordered_keys[i]])
            else:
                ans += ' ' + ' '.join(words_map[ordered_keys[i]])
                
        ans = ans[0].upper() + ans[1:]
        
        return ans

