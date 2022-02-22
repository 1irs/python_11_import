import json
import statistics

user_info: str = """
{
   "first_name": "Vladimir",
   "last_name": "Obrizan",
   "grades": [5, 5, 5, 4, 3]
}
"""

print(user_info)

user_object = json.loads(user_info)

print('user_object type: ', type(user_object))

print('First name:', user_object['first_name'])
print('Last name:', user_object['last_name'])
print('Grades: ', statistics.mean(user_object['grades']))

d1 = {
    'title': 'Python',
    'author': 'Mark'
}

print('Print : ', d1)
print('Json string: ', json.dumps(d1))