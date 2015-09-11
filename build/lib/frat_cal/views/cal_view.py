from flask import Blueprint, render_template
from flask.views import MethodView
 
blueprint = Blueprint('cal_view',__name__,template_folder='templates')

class ProspectiveView(MethodView):

	def get(self):
 		return render_template("calendar.html",type="planning")

class FinalizedView(MethodView):

	def get(self):
 		return render_template("calendar.html",type="Finalized")
 
 
blueprint.add_url_rule('/planning',view_func=ProspectiveView.as_view('Pro'))
blueprint.add_url_rule('/',view_func=FinalizedView.as_view('Fin'))
