def my_search(data, el):
    if len(data) == 0:
        return -1
    else:
        mid = len(data) // 2

        if el == data[mid]: 
            return mid
        else:
            if el < data[mid]:
                return my_search(data[:mid], el)
            else:
                return my_search(data[mid+1:], el)

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(my_search(test_list, 12))