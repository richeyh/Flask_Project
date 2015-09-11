from flask import Flask
from frat_cal.views.cal_view import blueprint as cal_blue
from flask.ext.sqlalchemy import SQLAlchemy
from frat_cal.extensions import DB
from frat_cal.models.cal_models import event
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')
DB = SQLAlchemy(app)
#blueprint registration
app.register_blueprint(cal_blue)
#admin registration
admin = Admin(app, name="Portal", template_mode='bootstrap3')
admin.add_view(ModelView(event, DB.session))
