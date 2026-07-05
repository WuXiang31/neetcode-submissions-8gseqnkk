class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n1 in nums:
            ## Find the second sum value
            n2 = target - int(n1)

            # check if the second sum value exist in the list
            for i in range(len(nums)):
                # find the index of the sum 1 and 2
                if nums[i] == int(n2):
                    inn1 = nums.index(n1)

                    # prevent the exist of multiple same value
                    if inn1 != i:
                        return [inn1, i]
