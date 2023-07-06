class Anagram:
    def __init__(self, word1): 
        self.word1_sorted = sorted([letter for letter in word1])
        
    def match(self, word_list): 
        return [word2 for word2 in word_list if sorted([letter for letter in word2]) == self.word1_sorted]
    

  
        
    
    
    








