def shellSort(array):
    n = len(array)
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


data = [9, 8, 3, 7, 5, 6, 4, 16, 1, 45, 75, 10, 85, 11, 1]
shellSort(data)
print('Sorted Array in Ascending Order:')
print(data)


def shellSort(arr):
	gap = len(arr) // 2 # initialize the gap

	while gap > 0:
		i = 0
		i + gap
		
		# check the array in from left to right
		# till the last possible index of i + gap
		while i + gap < len(arr):
	
			if arr[i] >arr[i + gap]:
				arr[i],arr[i + gap] = arr[i + gap],arr[i]
			
			i += 1

		
			# now, we look back from ith index to the left
			# we swap the values which are not in the right order.
			k = i
			while k - gap > -1:

				if arr[k - gap] > arr[k]:
					arr[k-gap],arr[k] = arr[k],arr[k-gap]
				k -= 1

		gap //= 2


# driver to check the code
a = [3, 7, 2, 8, 4, 6, 9, 1, 4]
print("input array:",a)

shellSort(a)
print("sorted array", a)