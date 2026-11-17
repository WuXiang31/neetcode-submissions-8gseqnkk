class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## check if the input list is empyt first
        if nums == []:
            return False

        ## sort the list
        ## and check the i element value is equal to next value then it is meant contain duplicate
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        ## done checking and no duplicate, just return false
        return False
