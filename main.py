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