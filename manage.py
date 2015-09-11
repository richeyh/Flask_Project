from application import app
from frat_cal.extensions import DB
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from frat_cal.models.cal_models import event

migrate = Migrate(app, DB)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()