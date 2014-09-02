list1 = 'One Two Three Four'

print '%r is not a list of 10 things, or a list at all, just a lousy string' %list1

list2 = list1.split(' ')
list3 = ['Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven']

while len(list2) < 10:
 item1 = list3.pop(0)
 print 'Adding: ', item1
 list2.append(item1)
 print 'There are now %d items' % len(list2)
 
print 'Here\'s the complete list: ', list2

print list2[4]
print list2[-1]
print list2.pop()
print ' '.join(list2)
print 'ThisGoesInTheMiddleOfEverything'.join(list2[3:8:2])