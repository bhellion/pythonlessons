print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
foobar = raw_input('How are you today? ')


print "So, you're %r old, %r tall and %r heavy. And you're feeling %r" % (
    age, height, weight, foobar)