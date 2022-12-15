class Solution:
    def seriesSum(self,n):
        n = n*(n+1)/2
        return int(n)
 

# Driver code 
if __name__ == "__main__": 		
    n = 5
    ob = Solution()
    ans = ob.seriesSum(n)
    print(ans)
# } Driver Code Ends