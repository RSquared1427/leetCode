class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)

        count = 1
        pre = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] is not 0:
                pre = nums[i+1]-nums[i]
                break
        if pre is not 0:
            count = count + 1
        for i in range(1,len(nums)-1):
            if pre * (nums[i+1]-nums[i]) < 0:
                count = count + 1
                pre = nums[i+1]-nums[i]
                
        return count

