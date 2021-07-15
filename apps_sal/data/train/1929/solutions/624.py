class StreamChecker:

    def __init__(self, words: List[str]):
        self.history = \"\"
        self.map = {}
        
        for word in words:
            curr_node = self.map
            for letter in word[::-1]:
                if letter not in curr_node:
                    curr_node[letter] = {}
                curr_node = curr_node[letter]
            curr_node['#'] = {}

    def query(self, letter: str) -> bool:
        self.history += letter

        curr_node = self.map
        for l in self.history[::-1]:

            if l not in curr_node:
                return False
                    
            curr_node = curr_node[l]
        
            if '#' in curr_node:
                return True
        
        return False



# class StreamChecker {

#     private String[] words;
#     private int[] pointers;
#     private TrieNode root;
#     private Set<TrieNode> nodes;
    
#     public StreamChecker(String[] words) {
#         this.words = words;
#         this.pointers = new int[words.length];
#         this.root = new TrieNode(' ');
#         this.nodes = new HashSet<>();
#         for (String word : words) {
#             TrieNode node = this.root.insert(word);
#         }
#         this.nodes.add(this.root);
#     }
    
#     public boolean query(char letter) {
#         boolean found = false;
#         // System.out.println(this.nodes.size());
#         // System.out.println(letter);
#         Set<TrieNode> next = new HashSet<>();
#         for (TrieNode node : this.nodes) {
#             // System.out.println(\"checking node \" + node.ch);
#             if (node.children[letter - 'a'] != null) {
#                 // System.out.println(\"not null\");
#                 TrieNode matched = node.children[letter - 'a'];
#                 // System.out.println(\"matched ch \" + matched.ch);
#                 if (matched.isTerminal) {
#                     found = true;
#                     // System.out.println(found);
#                 } else {
#                     next.add(matched);
#                 }
#             } 
#         }
#         this.nodes.clear();
#         this.nodes.add(this.root);
#         this.nodes.addAll(next);
#         return found;
#     }
    
#     private class TrieNode {
#         char ch;
#         TrieNode[] children;
#         boolean isTerminal;
        
#         public TrieNode(char character) {
#             ch = character;
#             children = new TrieNode[26];
#             isTerminal = false;
#         };
        
#         TrieNode insert(String word) {
#             TrieNode node = this;
#             for (int i = 0; i < word.length(); i++) {
#                 char ch = word.charAt(i);
#                 TrieNode next = null;
#                 if (node.children[ch - 'a'] == null) {
#                     next = new TrieNode(ch);
#                     node.children[ch - 'a'] = next;
#                 } else {
#                     next = node.children[ch - 'a'];
#                 }
#                 if (i == word.length() - 1) next.isTerminal = true;
#                 node = next;
#             }
#             return node;
#         }
#     }
    
# //     public boolean query(char letter) {
# //         // System.out.println(\"query ===\");
# //         boolean found = false;
# //         for (int i = 0; i < pointers.length; i++) {
# //             // System.out.println(\"word is \" + this.words[i]);
# //             if (this.words[i].charAt(this.pointers[i]) == letter) {
# //                 // match
# //                 this.pointers[i]++;
# //                 // System.out.println(\"pointer++\");
# //                 if (this.pointers[i] == this.words[i].length()) {
# //                     this.pointers[i] = findPointer(this.words[i].substring(0, this.words[i].length() - 1), this.words[i].substring(1));
# //                     found = true;
# //                 }
# //             } else {
# //                 // mo match
# //                 if (this.pointers[i] == 0) continue;
# //                 this.pointers[i] = findPointer(this.words[i].substring(0, this.pointers[i]), this.words[i].substring(1, this.pointers[i]) + letter);
# //             }
# //         }
        
# //         // System.out.println(Arrays.toString(this.pointers));
        
# //         return found;
# //     }
    
# //     private int findPointer(String base, String sub) {
# //         //  System.out.println(\"findPointer\");
# //         // System.out.println(base);
# //         // System.out.println(sub);
        
# //         if (base.equals(sub)) {
# //             // System.out.println(base.length());
# //             return base.length();
# //         } 
        
# //         for (int i = base.length() - 1; i >= 1; i--) {
# //             if (base.substring(0, i).equals(sub.substring(base.length() - i))) {
# //                 // System.out.println(i);
# //                 return i;
# //             }
# //         }
        
# //         // System.out.println(0);
# //         return 0;
# //     }
# }

# /**
#  * Your StreamChecker object will be instantiated and called as such:
#  * StreamChecker obj = new StreamChecker(words);
#  * boolean param_1 = obj.query(letter);
#  */
