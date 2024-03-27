import copy


def clone_list(lst):

    global clone
    if len(lst) != 0:
        clone = lst.copy()
        print("list is copied")
    else:
        print("not copied list is empty")
    return clone


lst1 = [1,3,4,56,7]
lst2 = []
print(clone_list(lst1))
print(clone_list(lst2))
