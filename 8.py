# Գրել ծրագիր, որը կգտնի NxM (N քանակությամբ տող և M քանակությամբ սյուն) չափանի մատրիցի մեծագույն
# արժեքը և կտպի էկրանին։

ls = [[12, 5, 143], [68, 3, 18], [96, 47, 23]]
max_value = 0
for i in ls:
	for j in i:
		if max_value < j:
			max_value = j

print(max_value)
