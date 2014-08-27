from sys import argv
from os.path import exists

script, from_file, to_file = argv

print 'Copying from %s to %s' % (from_file,to_file)

indata = open(from_file).read()

print 'The input file is %d bytes long' % len(indata)

print 'Existence of output file: %r' % exists(to_file)
raw_input('Ready = return, else ctrl-c')

out_file = open(to_file,'w')
out_file.write(indata)

out_file.close()