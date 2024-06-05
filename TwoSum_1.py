class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, i in enumerate(nums):
            if i in hash:
                hash[i] = index
        for i in hash:
            result = target - i
            if result in hash and hash[result] != hash[i]:
                return [hash[i], hash[result]]

    def twoSumOnePass(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, value in enumerate(nums):
            result = target - value
            if result in hash and index != hash[result]:
                return [index, hash[result]]
            hash[value] = index

        return []
