my_list2 = [1,2,3,4,5,6,7,8,9,10]
number_even = []
for number in my_list2:
    if(number % 2 == 0):
        number_even.append(number)

for even_number in number_even:
    print(even_number)
