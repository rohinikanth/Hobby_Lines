#List Methods

l=[4,5,6,7,8,7]

l.append(9)
print("Append: ",l)

l.extend([1,2])
print("Extend the list: ",l)

l.insert(2,1)
print("insert at index 2: ",l)

l.remove(1)
print("Remove: ",l)

l.pop()
print("POPED: ",l)

l.reverse()
print("Reversed list: ",l)

l.sort()
print("Sorted: ", l)


print("The index of elemnt 6: ",l.index(6))
print("Count 7: ", l.count(7))

l.clear()
print(l)


'''
Output LIST methods:
Append:  [4, 5, 6, 7, 8, 7, 9]
Extend the list:  [4, 5, 6, 7, 8, 7, 9, 1, 2]
insert at index 2:  [4, 5, 1, 6, 7, 8, 7, 9, 1, 2]
Remove:  [4, 5, 6, 7, 8, 7, 9, 1, 2]
POPED:  [4, 5, 6, 7, 8, 7, 9, 1]
Reversed list:  [1, 9, 7, 8, 7, 6, 5, 4]
Sorted:  [1, 4, 5, 6, 7, 7, 8, 9]
The index of elemnt 6:  3
Count 7:  2
[]
'''


#Tuple Methods
T = ('a',6,'Hai',[4,7],'a')
print(T)
print(T[3])
print(T[3][1])
print(T[2])
print(T[2][0])
print(T.count('a'))
print(T.index('a'))
'''
Output TUPLE methods:
('a', 6, 'Hai', [4, 7], 'a')
[4, 7]
7
Hai
H
2
0
'''
#Set Methodsd







