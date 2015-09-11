from flask import Blueprint, render_template
from flask.views import MethodView
from frat_cal.models.cal_models import get_events, get_event
 
blueprint = Blueprint('cal_view',__name__,template_folder='templates')

class ProspectiveView(MethodView):

	def get(self):
		events = get_events(2)
 		return render_template("calendar.html",type="planning",events=events)

class FinalizedView(MethodView):

	def get(self):
		events = get_events(1)
 		return render_template("calendar.html",type="Finalized",events=events)

class EventView(MethodView):

	def get(self, event_id):
		event = get_event(event_id)
		return render_template("event.html",event=event)
 
 
blueprint.add_url_rule('/planning',view_func=ProspectiveView.as_view('Pro'))
blueprint.add_url_rule('/',view_func=FinalizedView.as_view('Fin'))
blueprint.add_url_rule('/event/<event_id>',view_func=EventView.as_view('Event'))
