# dict of states and their abbreviation
states = {
 'Oregon' : 'OR',
 'California' : 'CA',
 'Florida' : 'FL',
 'New York' : 'NY'}
 
# dict of states and their cities
cities = {
 'CA' : 'San Fran',
 'FL' : 'Orlando'}
 
# add more to cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
 
# print some cities
print '-' *10
print 'NY State has: ', cities['NY']
print 'OR state has: ', cities['OR']
 
# print some states
print '-' *10
print 'California\'s abbreviation is: ', states['California']
print 'Oregon\'s abbreviation is: ', states['Oregon']
 
# print cities from the state name
print '-' *10
print 'California has: ', cities[states['California']]

# print every abbreviation
print '-' *10
for state,abbre in states.items():
 print '%s is abbreviated %s' %(state,abbre)

# print every city
print '-' *10
for abbre,city in cities.items():
 print '%s has %s' %(abbre,city)

print '-' *10
for state,abbre in states.items():
 print '%s is abbreviated %s and has %s' %(state,abbre,cities[abbre])

state = states.get('Texas')
if not state:
 print 'No Texas'
 
city = cities.get('TX', 'Does not exist')
print 'The city in \'TX\' is : %s' % city