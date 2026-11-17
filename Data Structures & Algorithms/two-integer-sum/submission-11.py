class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            secondValue = target - num
        
            if secondValue in seen: 
                return [seen[secondValue], i]
            
            seen[num] = i
