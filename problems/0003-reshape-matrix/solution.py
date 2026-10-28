import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	h=np.shape(a)
    if h[0]==new_shape[0] and h[1]==new_shape[1]:
		return a

	if h[0]!=new_shape[1] or h[1]!=new_shape[0]:
		return []
	c=[]
	e=[]
	count=0
	for i in range (new_shape[0]):
		d=[0]*new_shape[1]
		c.append(d)
	for i in a:
		e.extend(i)
    
	for i in range (new_shape[0]):
		for j in range (new_shape[1]):
			c[i][j]=e[count]
			count+=1
	return c

	


	