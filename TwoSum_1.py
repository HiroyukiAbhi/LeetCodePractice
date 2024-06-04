class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index,i in enumerate(nums):
            hash[i] = index
        for i in hash:
            result = target - i
            if result in hash and hash[result] != hash[i]:
                return [hash[i], hash[result]]

