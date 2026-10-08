class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check for equal length
        if len(s)!=len(t):
            return False
        #creating a hashmap for s
        s_map={}
        for char in s:
            if char in s_map:
                s_map[char]+=1
            else:
                s_map[char]=1
        
        #create a hashmap for t
        t_map={}
        for char in t:
            if char in t_map:
                t_map[char]+=1
            else:
                t_map[char]=1

        if s_map==t_map:
            return True
        else:
            return False
