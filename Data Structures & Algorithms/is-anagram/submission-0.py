class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1=[0]*26
        c2=[0]*26

        for char in list(s.lower()):
            pos=ord(char)-ord('a')
            c1[pos]+=1
        for char in list(t.lower()):
            pos=ord(char)-ord('a')
            c2[pos]+=1

        return c1==c2
        
            