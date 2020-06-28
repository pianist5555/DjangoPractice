import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print("Content-Type: text/plain")
print()

print("Welcome... CGI SCripts")
print("name is %s" % name)
print("email is %s" % email)
print("url is %s" % url)