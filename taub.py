import requests

students_url = "http://www.cs.technion.ac.il/people/graduate-students/"

# Lazy html parser to get the list of all students
def get_students_list(students_html):
	students = []
	for line in students_html.split('\n'):
		if line[:6] == '  <li>' and '/people/' in line:
			student = {}
			student['name'] = line.split('page for ')[1].split('"')[0]
			print(student['name'])
			students.append(student)

# Lazy html parser to get the office number
def get_office_number(html_str):
	pass

students_html = requests.get(students_url)
students_list = get_students_list(students_html.text)
exit()

for student in students_list:
	office_num = get_office_number(student['url'])
	student['office'] = office_num
	print(student['name'], student['program'], student['office'])