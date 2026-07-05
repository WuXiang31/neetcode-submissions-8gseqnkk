class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range( len(nums)):
            n2 = target - int(nums[i])
            for j in range(len(nums)):
                if i != j:
                    if nums[j] == int(n2):
                        return [i, j]


        