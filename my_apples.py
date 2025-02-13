import random 

john = 6
marry = 5
adam = 6
#print(john, marry, adam, sep=', ')

total_apples = (john + marry + adam)
print(f'{total_apples} apples counted')
if total_apples == 10:
    print('bad harvest season!!! ')
elif total_apples < 20:
    print('not so lucky season!!!')
elif total_apples > 20: 
    print('nice harvest season\nand i like it') 
else:
    print("counting is wrong")      
total_sum = (f'total number of apples is: {total_apples}')
print(total_sum)
print('thank you for your counting\nsee you next season')   
