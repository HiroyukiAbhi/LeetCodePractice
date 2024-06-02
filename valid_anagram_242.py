class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        if len(s) != len(t):
            return False

        for char, i in enumerate(s):
            hash_s[char] = 1 + hash_s.get(char, 0)
            hash_t[t[i]] = 1 + hash_t.get(t[i],0)
        for i in hash_s:
            if hash_s[i] != hash_t.get(i, 0):
                return False

        return True
    
            

