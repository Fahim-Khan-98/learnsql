import random
from models import User, engine
from sqlalchemy .orm import sessionmaker
from sqlalchemy import or_, and_, not_

Session = sessionmaker(bind=engine)

session = Session()


#  ************* using filter

# users = session.query(User).all()

# users_filtered = session.query(User).filter(User.age>28, User.name == 'ayon').all()


# print("User",len(users))
# print("Users Filtered",len(users_filtered))

# ************* using filter_by

# users_filter_by = session.query(User).filter_by(age=23).all()


# for user in users_filter_by:
#     print("user age ",user.age)

#  ************* using where

# user_where = session.query(User).where(User.age >=25 , User.name=='taj').all()
# print("Total User",len(user_where))
# for user in user_where:
#     print(f'{user.age} - {user.name}')


#  ************* using where -> OR
# user_where = session.query(User).where((User.age >=25) | (User.name=='taj')).all()
# user_where = session.query(User).where(or_(User.age >=25 , User.name=='taj' , User.id>4)).all()
# print("Total User",len(user_where))
# for user in user_where:
#     print(f'{user.age} - {user.name}')



#  ************* using where -> AND
# user_where = session.query(User).where(and_(User.age >=25 , User.name=='taj')).all()
# user_where = session.query(User).where((User.age>25) & (User.name == 'taj')).all()
# print("Total User",len(user_where))
# for user in user_where:
#     print(f'{user.age} - {user.name}')





#  ************* using where -> NOT
# user_where = session.query(User).where(not_(User.age >=25)).all()
# user_where = session.query(User).where((User.age>25)).all()
# user_where = session.query(User).where(not_(User.name == 'hia')).all()
# print("Total User",len(user_where))
# for user in user_where:
#     print(f'{user.age} - {user.name}')




# combine all 

user_combine = session.query(User).where(or_
                                         (not_(User.name == 'hia'),
                                          and_(User.age >20, User.age <70)
                                          )
                                        ).all()


print("Combine User",len(user_combine))
for user in user_combine:
    print(f'{user.age} - {user.name}')