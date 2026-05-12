class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                result = []
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result