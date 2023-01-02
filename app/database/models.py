import peewee
import settings

class User(peewee.Model):
    username = peewee.CharField(max_length=50,unique=True,null=False)
    password = peewee.CharField(max_length=50,unique=True,null=False)
    email = peewee.CharField(max_length=50,unique=True,null=False)
    active = peewee.BooleanField(default=True)

    class Meta:
        database = settings.CONNECTION 
        db_table = 'users'

    def __str__(self): return self.username 


class Task(peewee.Model):
    title = peewee.CharField(max_length=50)
    user = peewee.ForeignKeyField(User,backref='tasks')

    class Meta:
        database = settings.CONNECTION 
        db_table = 'tasks'

    def __str__(self): return self.title 

MODELS = [User,Task]
