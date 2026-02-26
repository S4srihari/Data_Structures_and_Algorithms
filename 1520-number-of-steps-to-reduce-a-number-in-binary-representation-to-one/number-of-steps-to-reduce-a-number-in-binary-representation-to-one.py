class Solution:
    def numSteps(self, s: str) -> int:
        seen = False
        n = len(s) 
        operations = 0
        for i in range(n-1,0,-1):
            if s[i] == '1' and not seen:
                operations += 2
                seen = True
            elif s[i] == '1' and seen:
                operations += 1
            elif s[i] == '0' and seen:
                operations += 2
            elif s[i] == '0' and not seen:
                operations += 1

        if seen and s[0] == '1':
            operations += 1
 
        return operations