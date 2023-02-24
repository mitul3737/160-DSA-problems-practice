#Brute force
#Time complexity : O(nlogn) for sorting + O(n) for iteration == O(nlogn)
#Space complexity: O(n) for our new list of length of the array
def sortedSquared(array):
    sortedSquares=[0 for _ in array] #space complexity becomes O(n)
    #arrding squared values to our new list
    for index in range(len(array)): #Time complexity O(n)
        value=array[index]
        sortedSquares[index]=value*value
    sortedSquares.sort() #sorting the squared list ; Time complexity: O(nlogn)
    return sortedSquares

array=[-4,3,2,1,9]
print(sortedSquared(array))