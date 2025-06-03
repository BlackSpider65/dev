odd = []
even = []
re = [even.append(i) if i%2==0 else odd.append(i) for i in range(1,10)]
print(f"The even number is: {even}")
print(f"The odd number is: {odd}")