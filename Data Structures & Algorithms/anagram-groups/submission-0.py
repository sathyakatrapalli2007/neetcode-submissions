class Solution:
    def groupAnagrams(self, strs: List[str]):
        mega_hash={}
        for word in strs:
            hash_list=[0]*26
            for ch in word:
                hash_list[(ord(ch)-97)%26]+=1
            if tuple(hash_list) in mega_hash:
                mega_hash[tuple(hash_list)].append(word)
            else:
                mega_hash[tuple(hash_list)]=[word]

        return list(mega_hash.values())
