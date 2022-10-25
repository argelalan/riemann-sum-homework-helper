import math


def func(var):
	return math.sin(var) # Change this to whatever function you need.


def trapezoidal(var, var_delta, step_size):
	"""Return estimate using the trapezoidal rule."""
	result = 0
	for i in range(step_size + 1):
		if i == 0 or i == step_size:
			result += func(var)
		else:
			result += 2 * func(var)
		var += var_delta
	
	return result * (var_delta / 2)


def midpoint(var, var_delta, step_size):
	"""Return estimate using the midpoint method."""
	result = 0
	for i in range(step_size):
		mid_var = var + (var_delta / 2)
		result += func(mid_var)
		var += var_delta

	return result * var_delta


def simpsons(var, var_delta, step_size):
	"""Return estimation using Simpson's rule."""
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


upper_bound = float(input('Enter value for upper bound: '))
lower_bound = float(input('Enter value for lower bound: '))
n = int(input('Enter step size: '))

delta = (upper_bound - lower_bound) / n
x = lower_bound

trap_result = trapezoidal(x, delta, n)
midpoint_result = midpoint(x, delta, n)
simpson_result = simpsons(x, delta, n)

print('Trapezoidal: ', trap_result)
print('Midpoint: ', midpoint_result)
print('Simpson: ', simpson_result)
