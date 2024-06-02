class Solution:
   #https://leetcode.com/problems/contains-duplicate/ 
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i, num in enumerate(nums):
            if num in hash:
                return true
            hash[num] = 1
        return false
