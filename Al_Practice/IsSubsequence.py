class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        s_new = ""
        for x in range(0, len(s)):
            while(i < len(t)):
                if(s[x]==t[i]):
                    s_new += s[x]
                    break
                else:
                    i = i+1
            i = i+1 
        if(s==s_new):        
            return True
        else:
            return False
            
s="axc"
t = "ahbgdc"
so = Solution()
print(Solution().isSubsequence(s,t))                  

