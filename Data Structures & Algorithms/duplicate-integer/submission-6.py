class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # put it into set (no duplicate)
        seen = set()

        ## if nums in the set (duplicate), True
        ## if nums in the set (duplicate), True
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                ##duplicate, True
                return True

        ## No duplicate, False
        return False
