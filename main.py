###Problem link: https://leetcode.com/problems/two-sum/
#Time complexity O(n); space O(n)
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
                return f"{self.hash_table[self.remaining]+1} {self.index+1}" #+1 because they wanted the position, not the index
                #self.index is the last index and it was incrementted . So, no need to increment.
            else:
                self.hash_table[value]= self.index  
                self.index+=1
        return "IMPOSSIBLE" #as mentioned in the code

val=input("").split(" ")
len_arr=int(val[0])
target=int(val[1])
arr=input("").split(" ")
array=[]
for i in arr:
    array.append(int(i))


abj=Solution()
print(abj.twoNumberSum(array,target))