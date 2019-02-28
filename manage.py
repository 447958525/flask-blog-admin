from flask_script import Manager
from app import create_app, db
from flask_migrate import MigrateCommand, Migrate


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    """Run deployment tasks."""
    from flask.ext.migrate import upgrade
    from app.models import Role, User

    upgrade()

    Role.insert_roles()
    User.add_self_follows()


if __name__ == '__main__':
    manager.run()
