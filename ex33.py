from sys import argv

script,upper_limit,interval_num, start_number = argv

def make_nums(up_num,int_num,start_num):

 foo = start_num
 numbers = []

 while foo < int(up_num):
  print 'At the top i is %d' % foo
  numbers.append(foo)
 
  foo += int_num
  print 'Numbers now: ', numbers
  print 'At the bottom i is %d' %foo

 print 'The numbers: '
 
 for num in numbers:
  print num
  
make_nums(int(upper_limit),int(interval_num),int(start_number))