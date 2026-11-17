class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            ## get the second value
            secondValue = target - nums[i]

            ## loop through the list and get the index
            for j in range(len(nums)):
                if nums[j] == secondValue:
                    if j != i:
                        return [i, j]