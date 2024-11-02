lst = ['mumbay', 'chicago', 'hyderabad', 'canberra']
print("length of list : ", len(lst))
print("first element : ", lst[0])
print("last element : ", lst[-1])

lst.append('moscow')
print("updated list : ", lst)

lst.remove('chicago')
print("updated list : ", lst)

lst.sort()
print("sorted list : ", lst)

lst.pop(1)
print("updated list : ", lst)

lst.reverse()
print("reversed list : ", lst)

print("multiplication on list : ", lst*12)

lst = lst[:2]
print("sliced list : ", lst)
lst.clear()
print("updated list : ", lst)