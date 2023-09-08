from models import db
import click
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = db
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    db.init_app(current_app)
    with current_app.app_context():
        db.create_all()


@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Database Initialized')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
