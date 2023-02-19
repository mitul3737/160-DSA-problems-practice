### time complexity O(nlogn); space complexity O(1)
def twoNumberSum(array,target):
    array.sort()
    left_pointer=0
    right_pointer=len(array)-1

    while left_pointer<right_pointer:
        sum_0=array[left_pointer] + array[right_pointer]  
        if sum_0==target:
            return [array[left_pointer],array[right_pointer]]
        elif sum_0 < target:
            left_pointer+=1
        elif sum_0 > target:
            right_pointer -=1
    return [] 

array=[8,-1,1,11,6,3]
target=1
print(twoNumberSum(array,target))