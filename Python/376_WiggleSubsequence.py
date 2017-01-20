class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
	norep = [num for num, _ in itertools.groupby(nums)]
       
        if len(norep)<2:
            return len(norep)
        count = 2
        pre = norep[1] - norep[0]
        for i in range(1,len(norep)-1):
            if pre * (norep[i+1]-norep[i]) < 0:
                count = count + 1
                pre = norep[i+1]-norep[i]

        return count
        
	def wiggleMaxLength(self, nums):
    	    norep = [num for num, _ in itertools.groupby(nums)]
    	    triples = zip(norep, norep[1:], norep[2:])
            return sum((b>a) == (b>c) for a, b, c in triples) + len(norep[:2])
