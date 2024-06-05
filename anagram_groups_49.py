class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        hashedList = []
        out = []
        for index, value in enumerate(strs):
            a = {}
            for i, v in enumerate(value):
                if v in a:
                    a[v] += 1
                else:
                    a[v] = 1
            if a in hashedList:

