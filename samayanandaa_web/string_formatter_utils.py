
def construct_subject(subject):
	return subject

def construct_body(first_name, last_name, date_of_birth, time_of_birth, place_of_birth, current_location, message):
	body = "<p>Full name (First Last): </font>" + " ".join([first_name, last_name]) + "</p><br>"
	body += "Date of Birth (Year, Month, Day): " + date_of_birth.strftime('%Y/%m/%d') + "<br>"
	body += "Time of Birth (Hour, Minute, Second): " + time_of_birth + "<br>"
	body += "Place of Birth: " + place_of_birth + "<br>"
	body += "Current Location: " + current_location + "<br>"
	body += "message: " + message + "<br>"
	return body