import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	ans = []
	for i in a:
		if len(i) != len(b):
			return -1
		c = np.dot(i,b)
		# print(c)
		ans.append(c)
	return ans
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass