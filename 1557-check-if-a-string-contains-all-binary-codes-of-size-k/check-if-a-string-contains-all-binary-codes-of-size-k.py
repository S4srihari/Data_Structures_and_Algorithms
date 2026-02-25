class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        uniques = set()
        for i in range(k,len(s)+1):
            uniques.add(s[i-k:i])
        return len(uniques) == 2**k