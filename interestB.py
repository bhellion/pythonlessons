# interestB.py - the miracle of compound interest

# First, we'll set up the variables we want to use.
principal = 10000.00 # Our starting amount
year = 2014 # This is the starting year for our table.
years = 10 # How many years are we saving up?
periods = 12 # Number of compounding periods per year
rate = 0.015 # This is our nominal annual percentage rate.

# Print the headers for our report:

# the old way:
# print "%4s\t%7s" % ("Year", "Balance")

# the new way:
print '{:4s}\t{:7s}'.format("Year", "Balance")

for n in range(years + 1):
	nest_egg = principal * ((1 + (rate / periods)) ** (periods * n))

	# the old way:
	# print "%4d\t$%8.2f" % (year, nest_egg)

	# the new way:
	print '{:4d}\t${:8.2f}'.format(year, nest_egg)
