#!/usr/bin/python36
import cgi
import cgitb
import pymysql as mydb
cgitb.enable()

print('Content-Type:text/html \n')
elements=cgi.FieldStorage()
cname=elements.getvalue('name') or ""
cindustry=elements.getvalue('indstry') or ""
hqaddress=elements.getvalue('headquarter') or ""
description=elements.getvalue('About') or ""
csize=elements.getvalue('size') or ""
smedias=elements.getvalue('social') or ""
ctype=elements.getvalue('type') or ""


smedia=",".join(smedias)

sql="INSERT INTO companyform"
sql+=" VALUES('"+ cname +"','"+ cindustry +"','"+ hqaddress +"','"+ description +"','"+ csize +"','"+ smedia +"','"+ ctype +"')"

try:
	conn = mydb.connect (host="localhost", user="team1", password="team1", database="team1")
	cursor=conn.cursor()
	cursor.execute(sql)
	conn.commit()

except mydb.Error as e:
	(errorNum,errorMsg)=e.args
	print('Database Error-'+ str(errorNum)+errorMsg)
	exit()

print("<font color=red>Your order has been saved sucessfully</font>")
cursor.close()
conn.close()


