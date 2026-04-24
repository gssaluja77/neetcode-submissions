class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = ""
        min_len = min(len(word1), len(word2))

        i = 0
        while i < min_len:
            merged_string += word1[i]
            merged_string += word2[i]
            i += 1
        
        if len(word1) > len(word2):
            merged_string += word1[i:]
        else:
            merged_string += word2[i:]
        
        return merged_string