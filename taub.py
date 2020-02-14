import requests

students_url = "http://www.cs.technion.ac.il/people/graduate-students/"

# Lazy html parser to get the list of all students
def get_students_list(students_html):
	students = []
	for line in students_html.split('\n'):
		if line[:6] == '  <li>' and '/people/' in line:
			student = {}
			student['name'] = line.split('page for ')[1].split('"')[0]
			student['url'] = line.split('/people/')[1].split('"')[0]
			students.append(student)
	return students

# Lazy html parser to get the office number
def get_office_number(student_html):
	for line in student_html.split('\n'):
		if 'Office:' in line:
			office_num = int(line.split('<dd>')[1].split('</dd>')[0])
			return office_num

students_html = requests.get(students_url)
students_list = get_students_list(students_html.text)

for student in students_list:
	student_url = 'http://www.cs.technion.ac.il/people/' + student['url']
	student_html = requests.get(student_url)
	office_num = get_office_number(student_html.text)
	if office_num:
		student['office'] = office_num
	else:
		student['office'] = 0

students_list.sort(key = lambda s: s['office'])
for student in students_list:
	if student['office']:
		print(student['office'], student['name'])