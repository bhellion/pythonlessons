from sys import argv

script,filename = argv

raw_input('We\'re going to erase %r. If you don\'t want to do that, use ctrl-c, else enter to continue. ' %filename)

print 'Opening the file...'
target = open(filename,'w')

print 'Truncating the file. Woops!'
target.truncate()

print 'Let\'s replace what we erased with some new lines'

line1 = raw_input('Line 1: ')
line2 = raw_input('Line 2: ')
line3 = raw_input('Line 3: ')

print 'Writing to the file...'

target.write(line1 + '\n')
target.write(line2)
target.write('\n')
target.write(line3 + '\n')

# target.open()

# print target.read()

target.close()