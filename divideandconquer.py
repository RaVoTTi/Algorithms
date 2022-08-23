
def sum(array):
    if not (array):
        return 0
    else:
        return array[0] + count(array[1:])

def max(array):
    if not (array):
        return 0
    else:
        maximum = max(array[1:])
        if( array[0] < maximum):
            return maximum
        else:
            return array[0]

def count(array):
    if not (array):
        return 0
    else:
        return 1 + count(array[1:])

def quicksort(array):

        lenght = len(array) - 1
        if(lenght <= 0):
            return array

        else:
            moreArray = []
            lessArray = []
            pivot = array[0]
            for index in array[1:]:
                if(index > pivot):
                    moreArray.append(index)
                else:
                    lessArray.append(index)
            # if(more == True):
            #     return (quicksort(moreArray) + [pivot] + quicksort(lessArray)) 
            # else:
            return (quicksort(lessArray) + [pivot] + quicksort(moreArray)) 

def quicksortGrok(array):

        lenght = len(array) - 1
        if(lenght <= 0):
            return array

        else:
            moreArray = []
            lessArray = []
            pivot = array[0]
            for index in array[1:]:
                if(index < pivot):
                    lessArray.append(index)

            for index2 in array[1:]:
                if(index2 > pivot):
                    moreArray.append(index2)

            return quicksortGrok(lessArray) + [pivot] + quicksortGrok(moreArray) 

            # if(more == True):
            #     return moreArray + [pivot] + lessArray
            # else:
    # lenght = len(array) - 1
    # if (lenght < 1):
    #     if not (array):
    #         return []
    #     else:
    #         return array[0]
    # elif (lenght == 2):
    #     return
    # else:

    #     return quicksort(array) + [] + quicksort(array) 
def multiplication(array):
    lenght = len(array)
    middle = int(lenght / 2)
    if not(array):
        return array
    elif(lenght == 1):
        return [array[0] * 2]
    else:
        # return array
        return multiplication(array[:middle]) + multiplication(array[middle:])
 


if __name__ == "__main__":
    arrayToSort = [123,123,3,21,12, 8,2,7,2,3,45, 231,12,23,21,5456,7,64,6,4,78,9,34,2345,745,32,5,6,0,8,9,6,3,5,2,1,465,5,54,2,4,2,1,3,3,5,3,1,5,7,9,7,6,6,5,4,3,3,2,2,2]
    
    # print(sum([1]))
    # print(max([123,123,2,3,21,12]))
    # print(count([123,123,2,3,21,12, 8,2,7,2,3,45]))

    # print(quicksort(arrayToSort))

    # print(quicksortGrok(arrayToSort))
    print(multiplication(arrayToSort))

