def is_empty(a):
    if len(a) == 0:
        print("list is empty")
    else:
        print("list is not empty")
    return a


lst1 = [1, 2, 3, 4, 5]
lst2 =[]
print(is_empty(lst1))
print(is_empty(lst2))
