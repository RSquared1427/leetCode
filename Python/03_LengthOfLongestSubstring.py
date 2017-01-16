class Solution(object):
    def lengthOfLongestSubstring(self, s):
	HashTable={}
        start = 0
        end = 0
        rtype = 0
        for i in range(len(s)):
            if s[i] not in HashTable:  
                HashTable[s[i]] = i
                end = i
            else: 
                for j in range(start, HashTable[s[i]]):
                    del HashTable[s[j]]                      
                start = HashTable[s[i]]+1
                HashTable[s[i]] = i
                end = i
            rtype = max(rtype, end-start+1)
        return rtype

aa = 'pwkkew'
example = Solution()
print(example.lengthOfLongestSubstring(aa))


