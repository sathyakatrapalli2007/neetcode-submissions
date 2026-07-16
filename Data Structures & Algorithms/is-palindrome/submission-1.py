class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=''
        for letter in s:
            if letter.isalnum():
                string+=letter.lower()
                
        pallin=True
        for i in range(len(string)//2):
            if string[i]!=string[len(string)-i-1]:
                pallin=False
                break
        
        return pallin