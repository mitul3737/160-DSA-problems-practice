#Problem : https://www.algoexpert.io/questions/non-constructible-change
#Solve: Here we have to find the minimum amount of change that we cannot create using the given coins
#Time Complexity: O(nlogn) as we are sorting the array
#Space Complexity: O(1) as we are not using any extra space
#Approach: We sort the array and then we start adding the coins to the change created and if the coin is greater than the change created+1 then we return the change created+1
#as that is the minimum amount of change that we cannot create using the given coins
#for example, we had [5,7,1,1,2,3,22] 
#we sort the array and we get [1,1,2,3,5,7,22]
#we start adding the coins to the change created and we get
#in the first iteration we add 1 to the change created and we get 1
#in the second iteration we add 1 to the change created and we get 2
#in the third iteration we add 2 to the change created and we get 4
#in the fourth iteration we add 3 to the change created and we get 7
#in the fifth iteration we add 5 to the change created and we get 12
#in the sixth iteration we add 7 to the change created and we get 19
#in the seventh iteration we add 22 to the change created and we get 41
#now we will return 19+1=20 as that is the minimum amount of change that we cannot create using the given coins
def nonConstructibleChange(coins_array):
    coins_array.sort()
    change_created=0
    for coin in coins_array:
        if coin>change_created+1:
            return change_created+1
        change_created+=coin
    return change_created+1
     
array=[5,7,1,1,2,3,22]
print(nonConstructibleChange(array))