from sys import argv

script, input_file = argv

def print_file(f):
	print f.read()
	
def file_rew(f):
	f.seek(0)
	
def print_line(line_num,f):
	print line_num, f.readline()
	
foo = open(input_file)

print_file(foo)

file_rew(foo)

fool = 1
print_line(fool,foo)

fool += 1
print_line(fool,foo)

fool += 1
print_line(fool,foo)