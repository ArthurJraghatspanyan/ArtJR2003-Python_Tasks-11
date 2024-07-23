# Գրել ծրագիր, որն օգտագործողին թույլ կտա մուտքագրել ամբողջ թվային զանգվածի էլեմենտների արժեքները և կգտնի զանգվածի ամենամեծ և ամենափոքր տարրերի ինդեքսների տարբերությունը:

ls = []
size = int(input("Enter size for your list: "))
for i in range(size):
	tmp = int(input(f"Enter your element for {i} position: "))
	ls.append(tmp)
print(f"Our original list is: {ls}")
max_value = ls[0]
min_value = ls[0]
max_index = 0
min_index = 0
for i in range(1, len(ls)):
	if max_value < ls[i]:
		max_value = ls[i]
		max_index = i
	if min_value > ls[i]:
		min_value = ls[i]
		min_index = i
print(f"Our maximum value is: {max_value}")
print(f"Our maximum index is: {max_index}")
print(f"Our minimum value is: {min_value}")
print(f"Our minimum index is: {min_index}")
print(f"Result is: {max_index - min_index}")
