from frat_cal.extensions import DB

class event(DB.Model):
	"""all attributes to represent an event see the 
	full calendar docs for more info
	type_ is custom field 1 is finalized 2 is prospective
	"""
	id = DB.Column(DB.Integer, primary_key=True)
	type_ = DB.Column(DB.Integer)
	title = DB.Column(DB.String(150), unique=True)
	start = DB.Column(DB.DateTime)
	end = DB.Column(DB.DateTime)
	allday = DB.Column(DB.Boolean)
	url = DB.Column(DB.String(150))
	source = DB.Column(DB.String(150))
	color = DB.Column(DB.String(20))
	backgroundColor = DB.Column(DB.String(20))
	borderColor = DB.Column(DB.String(20))
	textColor = DB.Column(DB.String(20))
	cost = DB.Column(DB.Integer())
	description = DB.Column(DB.Text())



def get_events(kind):
	""" given a kind of event an int either 
	1 for finalize or 2 for planning return array of all event objects
	"""
	ret = event.query.filter(event.type_ == kind).all()
	return ret

def get_event(event_id):
	""" returns event object given id
	"""
	ret = event.query.get(event_id)
	return ret
