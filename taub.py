students_url = ""

# Lazy html parser to get the list of all students
def get_students_list(html_str):
	return []

# Lazy html parser to get the office number
def get_office_number(html_str):
	pass

students_html = students_html # curl or smth
students_list = get_students_list(students_html)

for student in students_list:
	office_num = get_office_number(student['url'])
	student['office'] = office_num
	print(student['name'], student['program'], student['office'])