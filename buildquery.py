# setup time!!

from canvasapi import Canvas
from canvasapi.exceptions import BadRequest
from datetime import datetime
from zoneinfo import ZoneInfo

# get my token
with open("token", "r") as tokenfile:
    token = tokenfile.readline()

# setup url
url = "https://westminster.instructure.com/"

canvas = Canvas(url, token)

courses = filter(lambda x: x.name.endswith("23SP"), canvas.get_courses())
courses = list(courses)

i=0
print("Choose a course!")
for cor in courses:
    print(str(i)+": "+cor.name)
    i += 1

course = courses[int(input())]

print(course)

email = input("Tell me your email please! ")

user = course.get_users(search_term=email)[0] # not safe lol

print(user)

assgs = filter(lambda x: x.published, user.get_assignments(course))

i=0
print("Choose an assignment!")
for assg in assgs:
    print(str(i)+": "+assg.name)
    i += 1

assg = assgs[int(input())]

print(assg)
