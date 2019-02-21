students = ['sophia','amber','kady']
# print(students[1])
# print(students[-1])
foods = 'kbbq', 'burger', 'sushi'
kbbq, burger, sushi = foods
print(burger, sushi)
hometown = {
    'city': 'Los Angeles',
    'state': 'CA',
    'population': 100
}
print(f'I was born in {hometown["city"]}')

for key, val in hometown.items():
    print(f'{key} = {val}')

cohort = []
for num in range(3):
    cohort.append({'student': students[num],'fav_food':foods[num]})
print(cohort)


foodies = [food for food in foods if 'u' in food]
print(foodies)

