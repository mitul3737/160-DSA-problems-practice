#Time complexity O(n^2) ; space complexity O(1)
class  Solution(object):
    def twoNumberSum(self,array,target):
        self.code_array=array
        self.code_target=target
        for i in range(len(self.code_array)-1): #-1 because the last one no one left to add with it. So, we will skip it
            first_num=self.code_array[i]
            for j in range(i,len(self.code_array)):
                second_num=self.code_array[j]
                if first_num+second_num==self.code_target and (first_num!=second_num):
                    return [first_num,second_num]
        return []

array=[8,-1,1,11,6,3]
target=10
abj=Solution()
print(abj.twoNumberSum(array,target))
