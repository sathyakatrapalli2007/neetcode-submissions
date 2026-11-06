class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1

        for key in hashmap:
            if hashmap[key]>=len(nums)//2:
                return key
        