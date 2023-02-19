###Problem link: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoNumberSum(self,array, target):
        self.code_array=array
        self.code_target=target
        self.hash_table={}  #dictionary
        self.remaining=0
        self.index=0 #for index count
        #we can use dictionary as well hash_table={}
        for value in self.code_array:
          
            self.remaining=self.code_target-value
            #print(f"remaining: {self.remaining}")
            #print(self.hash_table)
            if self.remaining in self.hash_table.keys() and (self.hash_table[self.remaining]!=self.index): #to check enequal
                #print("Entered")
                ###(self.hash_table[self.remaining]!=self.index) here we checked if the remaining value's index and values index are same or not. If same, we won't take it. It means , we will avoid repeatation.
                return [self.hash_table[self.remaining],self.index] #self.index is the last index and it was incrementted . So, no need to increment.
            else:
                self.hash_table[value]= self.index  
                self.index+=1
        return []


array=array=[3,3]
target=6
abj=Solution()
print(abj.twoNumberSum(array,target))