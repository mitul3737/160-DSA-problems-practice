class Solution(object):
    def twoNumberSum(self,array, target):
        self.code_array=array
        self.code_target=target
        self.hash_table=[] #list
        self.remaining=0
        #we can use dictionary as well hash_table={}
        for i in self.code_array:
            self.remaining=self.code_target-i
            if self.remaining in self.hash_table and (self.remaining!=i):
                return [self.remaining,i]
            else:
                self.hash_table.append(i)
        return []


array=[3,2,4]
target=6
abj=Solution()
print(abj.twoNumberSum(array,target))