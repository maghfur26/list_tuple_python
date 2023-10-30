def myfunction(x):
    return x % 10

list1 = [12, 34, 23, 13]
print("List before sort: ", list1)
list1.sort(key=myfunction)
print("list after sort: ", list1)