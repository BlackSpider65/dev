odd = []
even = []
re = [even.append(i) if i%2==0 else odd.append(i) for i in range(1,10)]
print(f"The even number is: {even}")
print(f"The odd number is: {odd}")
print()
#Now modify the file 
# write the program to print only digit in the given list
print("Now modify the file")
l = [20,"ram",10,"sunny","dev",30]
fal = [i if type(i) == int else 0 for i in l]
print(f"The digit are: {fal}")