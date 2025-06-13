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

for i, v in enumerate(['tic', 'tac', 'toe']): # the position index and corresponding value can be retrieved at the same time
    print(i, v)


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

output enumerate():
0 tic
1 tac
2 toe
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


#Set Methods
a = set('abracadabra')
b = set('alacazam')

print(f"A: {a}\nB: {b}")

b.add('b')
print("Update B:",b)


b.add('a')
print("Update B with already existing element:",b)

a.remove('d')
print("Element d removed from A:",a)

b.add('z')
print("Update A:",a)

a.update('mk')
print("Using update method",a)

a.update('97')
print("Using update method",a)
'''
output:
A: {'d', 'a', 'r', 'b', 'c'}

B: {'l', 'm', 'a', 'z', 'c'}

Update B: {'l', 'm', 'a', 'z', 'b', 'c'}

Update B with already existing element: {'l', 'm', 'a', 'z', 'b', 'c'}

Element d removed from A: {'a', 'r', 'b', 'c'}

Update A: {'a', 'r', 'b', 'c'}

Using update method {'k', 'a', 'r', 'm', 'b', 'c'}
Using update method {'k', '9', 'a', 'r', 'm', '7', 'b', 'c'}
'''
#Set operations
s1={2,5,6,7,89,23,0,45,4}
s2={8,7,4,56,78,21,67,2}

print(f"SET1: {s1}\nSET2:{s2}")

print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference:", s1.difference(s2))

print("Is subset:", {8, 4}.issubset(s1))
print("Is subset:", {2, 4}.issubset(s1))

s1.clear()
print("Cleared Set1:", s1)
'''
output:
SET1: {0, 2, 4, 5, 6, 7, 45, 23, 89}
SET2:{2, 67, 4, 7, 8, 78, 21, 56}

Union: {0, 2, 67, 4, 5, 6, 7, 8, 45, 78, 21, 23, 56, 89}
Intersection: {2, 4, 7}
Difference: {0, 5, 6, 45, 23, 89}

Is subset: False
Is subset: True
Cleared Set1: set()
'''


#Dictionary methods

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

print("Keys: ",knights.keys())
print("Values: ",knights.values())


for k, v in knights.items(): #key and corresponding value can be retrieved at the same time
    print(k, v)

knights.update({'bahubali': 'the strong'})
print("Updated: ",knights)

knights.update({'devasena': 'the gorgeous'})
print("Updated: ",knights)

print("Check robin: ",knights.get('robin'))

knights.pop('devasena')
print("After pop: ",knights)

knights.clear()
print("Cleared Dict:", knights)

'''
Keys:  dict_keys(['gallahad', 'robin'])
Values:  dict_values(['the pure', 'the brave'])

gallahad the pure
robin the brave

Updated:  {'gallahad': 'the pure', 'robin': 'the brave', 'bahubali': 'the strong'}

Updated:  {'gallahad': 'the pure', 'robin': 'the brave', 'bahubali': 'the strong', 'devasena': 'the gorgeous'}

Check robin:  the brave

After pop:  {'gallahad': 'the pure', 'robin': 'the brave', 'bahubali': 'the strong'}

Cleared Dict: {}

'''







