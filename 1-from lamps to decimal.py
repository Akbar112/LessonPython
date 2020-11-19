lamp1 = input('Status Lampu 1: ')
lamp2 = input('Status Lampu 2: ')
lamp3 = input('Status Lampu 3: ')
value = 0
if lamp1 == 'on':
    value +=4
if lamp2 == 'on':
    value +=2
if lamp3 == 'on':
    value +=1
print(f'Nilainya adalah {value}')