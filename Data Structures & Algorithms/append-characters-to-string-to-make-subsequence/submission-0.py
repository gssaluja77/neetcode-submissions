class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        len_s = len(s)
        len_t = len(t)

        i, j = 0, 0

        while i < len_s and j < len_t:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t[j:])