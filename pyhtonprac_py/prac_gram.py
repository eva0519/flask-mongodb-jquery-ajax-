a = 'bumkyu'
b = 'lee'

a_list = ['tkrhk', '배', 'rka']

print(a + b)
print(a_list[2])

a_list.append('tnqkr')
print(a_list)

a_dict = {'a': 'b',
          'c': 21}

print(a_dict)


def sum(a, b):
    print('ejgkwk')
    return a + b


result = sum(1, 2)
print(result)


def is_adult(age):
    if age > 20:
        print('yes')
    else:
        print('no')


is_adult(15)

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

count = 0

for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for ppp in people:
    if ppp['age'] > 20:
        print(ppp['name'])
