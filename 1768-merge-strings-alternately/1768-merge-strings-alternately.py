class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        text = []
        max_len = max(len(word1), len(word2))

        for i in range(max_len):
            if i < len(word1): 
                text.append(word1[i])
            if i < len(word2):
                text.append(word2[i])
        return "".join(text) 
