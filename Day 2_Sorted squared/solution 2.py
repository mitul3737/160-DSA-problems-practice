#Solve 2 : (Only works if we are alredy provided a sorted  array)
###Here we will set left pointer to the 1st index and right to the last and start comparing in the sense of their absolute values.
# [-7,-4,1,3,4,9]
#first we have left_pointer value = -7 and right_pointer_value=9, after comparing their absolute value, we see abs(9) > abs(-7); Now we will change the right pointer value
#SortedSquares=[0,0,0,0,0,81]
#now left pointer value= -7 and right pointer value= 4; here we get abs(-7)>abs(4)
#SortedSquares=[0,0,0,0,49,81]
#............ So, this is how we will proceed
def sortedSquaredArray(array):
    sortedSquares= [0 for _ in array]
    #print(sortedSquares)

    left_pointer=0 #assigning the left pointed to the 1st index
    right_pointer=len(array)-1 #keeping the right pointed to the last index

    for index in reversed(range(len(array))): #to assign values from last to first (in a reverse order)
        
        left_pointer_value=array[left_pointer]
        right_pointer_value=array[right_pointer]

        if abs(left_pointer_value)>abs(right_pointer_value):
            sortedSquares[index]=left_pointer_value*left_pointer_value
            left_pointer+=1
        else:
            sortedSquares[index]=right_pointer_value*right_pointer_value
            right_pointer-=1

    return sortedSquares
    
#array=[3,-4,2,9,1,-7]
array=[-7,-4,1,3,4,9] #Already sorted
print(sortedSquaredArray(array))
