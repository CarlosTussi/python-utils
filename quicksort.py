mylist = [10, 5, 8, 15, 20, 3, 7, 25, 30, 12, 18, 1, 23, 9, 14, 6, 19, 2, 11, 4, 22, 28, 17, 21, 27, 16, 29, 13, 24, 26]
mylist2 = [10,5,8,15,28,4,2]

def quicksort(mylist):
    
    if(len(mylist) == 0):       #If empty list, return empty list
        return []
    elif(len(mylist) == 1):     #If 1 element in the list, already sorted
        return [mylist[0]]
    elif(len(mylist)> 1):       
        last_index = len(mylist)-1      #Chose the pivot (last element)
        pivot = mylist[last_index]
        swapMarker = 0                  #Initialize the swap marker
        for i in range(len(mylist)):    #For all elements of the current list
            if (mylist[i] < pivot):     #If element < pivot:
                if(i != swapMarker):    #If we need to swap the current element with another one bigger than the piovt before
                    temp = mylist[swapMarker]
                    mylist[swapMarker] = mylist[i]
                    mylist[i] = temp
                swapMarker +=1          #Update the swapmarker
            elif(mylist[i] == pivot):   #If we reached the pivot
                if(i != swapMarker):    #Check if pivot needs to be swapped at the swap marker position
                    temp = mylist[swapMarker]
                    mylist[swapMarker] = pivot
                    mylist[i] = temp

        return quicksort(mylist[:swapMarker]) + [pivot] + quicksort(mylist[swapMarker+1:])      #Recursive call with the list splitted
        


print(quicksort(mylist))