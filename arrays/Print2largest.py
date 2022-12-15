class Solution:

	def print2largest(self,arr, n):
		m = max(arr)
		output = -1
		for item in arr:
		    if(item!=m) and (item>output):
		        output = item
		return (output)
		
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends