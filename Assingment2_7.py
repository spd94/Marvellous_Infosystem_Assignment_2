def print_pattern(n):	
	i=0
	print("Output :")
	while(i<n):
		j=0
		k=1
		while(j<n):
			print(k,end=" ")
			k+=1
			j+=1
		print("")
		i+=1
print("Input :",end=" ")
x=int(input())
print_pattern(x)