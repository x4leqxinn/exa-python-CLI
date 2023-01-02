#!/usr/bin/venv python
import click

# Create a group commands
@click.group()
def main(): pass

@main.command()
def say():
    print('Hello world!')

if __name__ == '__main__':
    main()