#Time Complexity:: O(2*n)-traversing all the elements in the 2D matrix twice
#Space Complexity:: O(n)-new result array is created
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for i in range(len(nums)): 
            index = abs(nums[i])-1 #starting with 1 so index of number should be number index-1
        
            if nums[index]>0: #if the number is positive we change the sign to -1 to mark it's presence
                nums[index]*= -1
        
        for j in range(len(nums)):
            if nums[j]>0: #second time traversing through nums check all the positive numbers
                result.append(j+1) #numbers that aren't present have positive values in index, so they are appended to result
        return result