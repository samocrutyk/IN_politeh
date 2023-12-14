number=input("введіть номер\n")
p_num=number[::-1] #початок кінець та крок
if p_num == number:
    print("це поліндром")
else:
    print ("не поліндром")