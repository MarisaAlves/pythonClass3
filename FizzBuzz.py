#!/usr/bin/env python3

for item in range(0,100):
	if item % 3 == 0  && item %5 == 0:
		print('FizzBuzz)
	elif item % 3 == 0:
		print('Fizz')
	elif item %5 == 0:
		print('Buzz')
	else:
		print(item)
