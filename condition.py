# for loop to calculate sum
sum = 0
for i in range(5):
    sum += i
    print sum

# while loop to calculate sum, the same result above
i = 0
while (i < 5):
    sum += i
    print sum
    i += 1

a = []
for i in range(5):
    a.append(i)
    
print 'a =', a    
print 'len of a', len(a)

# adding 1 to each item of the list
for i in range(len(a)):
    a[i] += 1
    
print 'new a =', a

# list operations. 
# append list
a_list = []
for i in range(5):
    a_list.append(i)
    
print a_list

# insert a item into a list
a_list.insert(1, 'a')
print a_list
    
# delete an item in a list    
a_list.pop(5)
print a_list

# extend an item to the end of a list
a_list.extend("a")
print a_list

# reverse a list
a_list.reverse()
print a_list

# copy an entire list
b = a_list[:]
print b

# c reference to a_list list.
c = a_list
print c

# extend an item in b won't affect 
# a_list bc b has its own copy of a_list
b.extend('b')
print b

# insert 
c[1] = 'b'
print a_list
print c

    
