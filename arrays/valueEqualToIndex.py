class Solution:

	def valueEqualToIndex(self,arr, n):
	    output =[]
		for i, a in enumerate(arr):
		    if(a==i+1):
		        output.append(i+1) 
		        
		return output



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1
