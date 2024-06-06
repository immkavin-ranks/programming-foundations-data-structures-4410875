def find_second_smallest(my_list):
    if len(my_list) > 1:
        sorted_list = sorted(my_list)
        return sorted_list[1]
    return None
    

print(find_second_smallest([5, 8, 3, 2, 6]))
