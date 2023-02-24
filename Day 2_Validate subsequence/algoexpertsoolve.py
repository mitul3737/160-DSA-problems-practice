#Time complexity O(n); here n is the length of array
#space complexity O(1); no need to add additional spaces.
def isValidSubsequence(array, sequence):
    seqIndex=0 #setting index for sequence to 0
    for value in array:
        #print(value) #checking each value from the array
        if seqIndex== len(sequence):#once all values from sequence is checked, it breaks
            break
        if sequence[seqIndex]==value:
            #print(value) #checking if any value maches
            seqIndex+=1 #once a value from sequence matches, we go to the next value of sequence
    return seqIndex==len(sequence)