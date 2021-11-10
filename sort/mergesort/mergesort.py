a = [3, 7, 2, 8, 4, 6, 9, 1, 4]

def  mergesort(list: list) -> list:
    if len(list) > 1:
        middle = len(list)//2
    # mergesort both halves
        left_l = list[:middle]
        right_l = list[middle:]
        mergesort(left_l)
        mergesort(right_l)
    # merge the halves
        merge(list, left_l, right_l)
    return list

def merge (list: list, left: list, right: list) -> list:
    n1 = len(left)
    n2 = len(right)
# Create temp lists
    # Merge the temp lists back
    i=0
    j=0
    k=0
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            list[k] = left[i]
            i+=1
        else:
            list[k] = right[j]
            j+=1
        k+=1
    # Copy the remaining elements of
    # Left, if there are any
    while i < n1:
        list[k] = left[i]
        i+=1
        k+=1
    #Copy the remaining elements of
    #Right, if there are any
    while j < n2:
        list[k] = right[j]
        j+=1
        k+=1
    return list
    
print(mergesort(a))