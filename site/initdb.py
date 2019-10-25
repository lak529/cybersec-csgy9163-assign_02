from app import db
from app.models import User

db.create_all()

u = User(username='luna', email='eightfold.witch@gmail.com')
u.setpw('test')
db.session.add(u)
db.session.commit()