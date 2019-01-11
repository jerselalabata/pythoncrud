import pymysql 
conn=pymysql.connect(
	host = "localhost",
	user = "jerselll",
	password = "jersel123456",
	db = "ex"
	)

c=conn.cursor()      
city=raw_input("Enter city name :")
c.execute("insert into city (city_name) values (%s)",(city))

c.execute("select * from city") 
rows=c.fetchall() 
for row in rows:
    print row dno=input("Enter id you want to delete :")
c.execute("delete from city where city_id='%s'",(dno))

eno=input("Enter the id you want to UPDATE :")
cityName=raw_input("Enter name you want to change :");
update=("update city set city_name=%s where city_id=%s")
c.execute(update,(cityName,eno))

c.execute("select * from city") 
rows=c.fetchall() 
for row in rows:
    print row

conn.commit() 
conn.close() 
print "Data are finised"