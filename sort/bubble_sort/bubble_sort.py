to_sort_list = [2,5,7,4,8,1]

def bubble_sort(list: list) -> list:
    swaps = False
    for i in range(len(list) - 1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            swaps = True
    if swaps:
        bubble_sort(list)
    return list

print(bubble_sort(to_sort_list))
