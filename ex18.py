def print_many(*args):
	arg1,arg2,arg3 = args
	print 'arg1: %r, arg2: %r, arg3: %r' %(arg1,arg2,arg3)

def print_two(arg1, arg2):
	print 'arg1: %r, arg2: %r' %(arg1,arg2)
	
def print_none():
	print 'Take no variables!'
	
print_many('One fish','Two fish','Red fish, blue fish')
print_two('Bob','Bill')
print_none()