from math import cos


def func(var):
	f_prime = (3 * (var ** 2)) / (1 + (var ** 3))
	return (1 + (f_prime ** 2)) ** (1 / 2)


def trapezoidal(var, var_delta, step_size):
	result = 0
	for i in range(step_size + 1):
		if i == 0 or i == step_size:
			result += func(var)
		else:
			result += 2 * func(var)
		var += var_delta
	
	return result * (var_delta / 2)


def midpoint(var, var_delta, step_size):
	result = 0
	for i in range(step_size):
		mid_var = var + (var_delta / 2)
		result += func(mid_var)
		var += var_delta

	return result * var_delta


def simpsons(var, var_delta, step_size):
	result = 0	
	for i in range(step_size + 1):
		if i == 0 or i == step_size:
			result += func(var)
		elif i % 2 == 0:
			result += (2 * func(var))
		elif i % 2 == 1:
			result += (4 * func(var))
		var += var_delta
	
	return result * (var_delta / 3)


upper_bound = int(input('Enter value for upper bound: '))
lower_bound = int(input('Enter value for lower bound: '))
n = int(input('Enter step size: '))

delta = (upper_bound - lower_bound) / n
x = lower_bound

trap_result = trapezoidal(x, delta, n)
midpoint_result = midpoint(x, delta, n)
simpson_result = simpsons(x, delta, n)

print('Trapezoidal: ', trap_result)
print('Midpoint: ', midpoint_result)
print('Simpson: ', simpson_result)
