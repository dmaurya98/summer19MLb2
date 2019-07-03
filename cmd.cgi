#!/usr/bin/python3

import cgi
import cgitb
import subprocess
import os

# to show comman error in webbrowser
cgitb.enable()

print("Content-type:text/html")
print()

webdata = cgi.FieldStorage() # this will collect all the html code with data

# now extraction value of X
data = webdata.getvalue('x')

# sending output of client via web server
print("<pre>")
print(os.system('cal'))
print("</pre>")

