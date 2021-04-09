def bubble_sort(list):
    #We go through the list as many times as there are elements
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                #swap
                list[j], list[j + 1] = list[j + 1], list[j]
                
list = [19, 25, 35, 21, 17, 36, 28, 1, 14, 8, 4]
print('Unsorted list')
print(list)
bubble_sort(list)
print('Sorted list')
print(list)