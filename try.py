

import pymysql 
conn=pymysql.connect(
	host = "localhost",
	user = "jersell",
	password = "jersel12345",
	db = "python"
	)
c=conn.cursor()

task=1
while(task!=0):
    print "==============================================";
    print "0. Exit";
    print "1. Insert Data";
    print "2. Show Data";
    print "3. Delete Data";
    print "4. Update Data";
    print "==============================================";
    task=input("Enter your choice : ");
    print "==============================================";
    if(task==1):
        # Insert Data Into table
        name=raw_input("Enter Name :")
        num=raw_input("Enter Number :")
        query = ("INSERT INTO `contacts` (`name`,`number`)  VALUES (%s,%s)")
        c.execute(query,(name,num))

        conn.commit()
    elif(task==2):
        # Select Data from Table
        print "===========After Inserting data records are===========";
        c.execute("select * from contacts")
        rows=c.fetchall()
        for row in rows:
            print row
        print "==============================================";

     
    elif(task==3):
        # Delete Data from database
        print "===========Select ID===========";
        c.execute("select * from contacts")
        rows=c.fetchall()
        for row in rows:
            print row
       	num = input("Select ID to delete :")
       	c.execute("DELETE FROM contacts WHERE id='%s'",(num))

       	conn.commit()
        print "==============================================";


    elif(task==4):
    	# update contacts
        print "===========Select ID===========";
        c.execute("select * from contacts")
        rows=c.fetchall()
        for row in rows:
            print row
        na = input("Select ID to update :")
        print "1. Name";
        print "2. Number";
        edit = input("Select Number to Update :")
        if(edit==1):
        	name1 = raw_input("input Name :")
        	update = ("UPDATE contacts SET name=%s WHERE id =%s")
        	c.execute(update,(name1,na))

        	conn.commit()
        elif(edit==2):
        	num1 = raw_input("input Number :")
        	update = ("UPDATE contacts SET number=%s WHERE id =%s")
        	c.execute(update,(num1,na))

        	conn.commit()

        else:

        	print "Wrong Choice!!"

    else:

    	print "GOOD BYE!!!!!"






