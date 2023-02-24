#Time complexity O(n); here n is the length of array
#space complexity O(1); no need to add additional spaces.
#Problem: https://leetcode.com/problems/is-subsequence/
class Solution: 
    def isSubsequence(self,sequence, target_string):
        self.seqIndex=0 #setting index for sequence to 0
        for value in target_string:
            #print(value) #checking each value from the array
            if self.seqIndex== len(sequence):#once all values from sequence is checked, it breaks
                break
            if sequence[self.seqIndex]==value:
                #print(value) #checking if any value maches
                self.seqIndex+=1 #once a value from sequence matches, we go to the next value of sequence
        return self.seqIndex==len(sequence)

s="abc"
t="ahbgdc"
obj=Solution()
print(obj.isSubsequence(s,t))