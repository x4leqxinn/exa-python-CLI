#!/usr/bin/venv python
import click
from app.database.models import MODELS, User, Task
import settings

# Create a group commands
@click.group()
def main(): pass

# Command 
# Args
# Options
# Flags -> Bool

@main.command()
def create_tables():
    with settings.CONNECTION:
        settings.CONNECTION.create_tables(MODELS)
    print('--- Tablas creadas ---')

@main.command()
@click.argument('username')
@click.option('--password','-p',prompt='Enter password',hide_input=True)
@click.option('--email','-e',default='jorge@gmail.com')
@click.option('--active','-a',is_flag=True,default=True)
def create_user(username,password,email,active):
    user = User.create(username=username,password=password,email=email,active=active)
    if user.id:
        print('Usuario creado exitosamente!')

@main.command()
@click.argument('title')
@click.argument('username')
def create_task(title,username): 
    user = User.select().where(User.username == username).first()
    if user:
        task = Task.create(title=title, user=user)
        if task.id: print('Tarea creada con exito!')

@main.command()
@click.argument('username')
def list_tasks(username):
    user = User.select().where(User.username == username).first()
    if user: 
        for task in user.tasks: print(task)


if __name__ == '__main__':
    main()