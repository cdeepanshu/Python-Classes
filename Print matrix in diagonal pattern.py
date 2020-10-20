# Python 3 program to print matrix in diagonal order 
MAX = 100

def printMatrixDiagonal(mat, n): 
	# Initialize indexes of element to be printed next 
	i = 0
	j = 0
	k = 0
	# Direction is initially from down to up 
	isUp = True

	# Traverse the matrix till all elements get traversed 
	while k<n * n: 
		# If isUp = True then traverse from downward 
		# to upward 
		if isUp: 
			while i >= 0 and j<n : 
				print(str(mat[i][j]), end = " ") 
				k += 1
				j += 1
				i -= 1

			# Set i and j according to direction 
			if i < 0 and j <= n - 1: 
				i = 0
			if j == n: 
				i = i + 2
				j -= 1

		# If isUp = 0 then traverse up to down 
		else: 
			while j >= 0 and i<n : 
				print(mat[i][j], end = " ") 
				k += 1
				i += 1
				j -= 1

			# Set i and j according to direction 
			if j < 0 and i <= n - 1: 
				j = 0
			if i == n: 
				j = j + 2
				i -= 1

		# Revert the isUp to change the direction 
		isUp = not isUp 

# Driver program 
if __name__ == "__main__": 
	mat = [[1, 2, 3], 
		[4, 5, 6], 
		[7, 8, 9] ] 

n = 3
printMatrixDiagonal(mat, n) 

# This code is contributed by Chitra Nayal 
