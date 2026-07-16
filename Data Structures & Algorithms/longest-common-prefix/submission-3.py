class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_letters=[]
        for i in range(200):
            letters=[]
            for words in strs:
                if i<len(words):
                    letters.append(words[i])
            if len(letters) != len(strs):
                break
            if letters==list(letters[0]*len(strs)):
                common_letters.append(letters[0])
            else:
                break
        return ''.join(common_letters)

            
            
            

            
        


        