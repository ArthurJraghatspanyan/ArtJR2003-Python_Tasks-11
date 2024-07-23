#Գրել ծրագիր, որը կստուգի երկու նույն չափի զանգվածները նույնն են, թե ոչ։
#Այսինքն արդյոք բոլոր համապատասխանող ինդեքսներով արժեքները համընկնում են, թե ոչ։

ls1 = [1, 2, 3, 4]
ls2 = [1, 2, 3, 4]

if len(ls1) == len(ls2):
	print("Yes for lists sizes")
	for i in range(len(ls1)):
		if ls1[i] == ls2[i]:
			print("Yes for list elements")
			break
		else:
			print("No for list elements")
			break
else:
	print("No for lists sizes")


