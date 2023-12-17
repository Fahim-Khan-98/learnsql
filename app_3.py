import random
from models import User, engine
from sqlalchemy .orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()


# Create
# names = ['bshora', 'repon', 'ayon', 'taj']
# ages = [29, 27, 23, 45]


# for x in range(20):
#     user  = User(name=random.choice(names), age=random.choice(ages))
#     session.add(user)
# session.commit()


# query all users orderd by age (ascending)


# users = session.query(User).order_by(User.age).all()

# for user in users:
#     print(f'user {user.name} age {user.age} id {user.id}')
    
# query all users orderd by age (decending)


users = session.query(User).order_by(User.name).all()

for user in users:
    print(f'user {user.name} age {user.age} id {user.id}')