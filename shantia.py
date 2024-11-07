data=[
    { 'id':1, 'name': 'alice', 'score':3 },
    { 'id':2, 'name': 'bob', 'score':7.87 },
    { 'id':3, 'name': 'charlie', 'score':9.1 },
    { 'id':4, 'name': 'david', 'score':11 },
    { 'id':5, 'name': 'eve', 'score':8 },
    { 'id':6, 'name': 'frank', 'score':9 },
    { 'id':7, 'name': 'grace', 'score':9.2 },
    { 'id':8, 'name': 'hanna', 'score':13 },
    { 'id':9, 'name': 'isaac', 'score':17 },
]

for item in data:
    if item['score'] >10:
        print(f"{item['name']} with score {item['score']} passed")
    elif item['score'] < 10 and item['score'] > 9:
        print(f"{item['name']} with score {item['score']} passed with thanks")
    else:
        print(f"{item['name']} with score {item['score']} has been outed")