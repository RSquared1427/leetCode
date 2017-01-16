class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(nums)):
            hashTable[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in hashTable and i != hashTable[target - nums[i]]:
                print([i, hashTable[target-nums[i]]])
                return [i, hashTable[target-nums[i]]]
        print("Nothing is fund!")
        return []



sample = Solution()
sample.twoSum([1,2,3,4], 7)

