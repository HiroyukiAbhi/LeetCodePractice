class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        for stri in strs:
            chars = [0] * 26
            for i in stri:
                chars[ord(i) - ord("a")]
            hash[tuple(chars)].append(stri)
        return hash.values
