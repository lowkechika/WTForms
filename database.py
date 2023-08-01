user_details = {
    0: {
        'user_email': 'admin@email.com',
        'username': 'admin',
        'password': '123456789'
    },
    1: {
        'user_email': 'can@gmail.com',
        'username': 'can',
        'password': '5545543789'
    },
    2: {
        'user_email': 'adam@gmail.com',
        'username': 'adam',
        'password': '77734556789'
    }
}

# for x in user_details:
#     if 'adam' in x['username']:
#         print(x['password'])

for x in user_details:
    print(user_details[x]['username'])
    if 'adam' in user_details[x]['username']:
        print('Found')

