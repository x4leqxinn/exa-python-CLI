from decouple import config
import peewee

CONNECTION = peewee.MySQLDatabase(
        config('DATABASE_NAME'),
        user=config('DATABASE_USER'),
        passwd=config('DATABASE_PASSWORD'),
        host=config('DATABASE_HOST'),
        port=int(config('DATABASE_PORT'))
    )
