from models import User, engine
from sqlalchemy .orm import sessionmaker


Session = sessionmaker(bind=engine)

session = Session()

# create


# user1 = User(name="hia", age=23)
# session.add(user1)
# session.commit()

# user1 = User(name= "Fahad Khan", age=24)
# user2 = User(name= "Foyaz Khan", age=21)
# user3 = User(name= "satvia", age=23)
# user4 = User(name= "borsha", age=29)
# session.add(user1)
# session.add_all([user2,user3,user4])
# session.commit()

# Read
# users = session.query(User).all()
# users = users[0]
# print(users.id)
# print(users.name)
# print(users.age)

# for user in users:
#     print(f'USER ID : {user.id} USER NAME : {user.name} AGE : {user.age}')


# Update
# users = session.query(User).filter_by(id=1).one_or_none()

# users.name = "fahim khan"
# users.age = 28
# session.commit()


# users = session.query(User).filter_by(age=22).one_or_none()
# print(users)


# Delete 
# users = session.query(User).filter_by(age=23).first()
# session.delete(users)
# session.commit()
