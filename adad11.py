import pymysql
connection = pymysql.connect(
    host = 'localhost',
    user = 'rov11',
    password = 'rov123',
    db = 'rov',
)

cursorr = connection.cursor()

task = 1
while(task != 0):
    print "0. Exit";
    print "1. Insert Data";
    print "2. Show Data";
    print "3. Delete Data";
    print "4. Update Data";
    print "_____________________";
    task = input("Enter your choice : ");
    print "_____________________";
    if(task == 1):
        #Insert Data to Table `addr`
        name = raw_input("Enter Name : ")
        address = raw_input("Enter Addres : ")
        sql = ("INSERT INTO `addr` (`name`,`address`)  VALUES (%s,%s)")
        cursorr.execute(sql, (name,address))

        connection.commit()
    elif(task == 2):
        #Select Data from Table `addr`
        print "____Data that you insert earlier_____";
        cursorr.execute("select * from addr")
        rows=cursorr.fetchall()
        for row in rows:
            print row
        print "___________________";

    elif(task == 3):
        #Delete Data from Table `addr`
        print "_______Select ID__________";
        cursorr.execute("select * from addr")
        rows = cursorr.fetchall()
        for row in rows:
            print row
       	address = input("Select ID to delete : ")
       	cursorr.execute("DELETE FROM addr WHERE id = '%s'",(address))

       	connection.commit()
        print "______Delete Data from Table `addr`_____";

    elif(task == 4):
    	#Update data from Table `addr`
        print "_______Select ID_______";
        cursorr.execute("select * from addr")
        rows = cursorr.fetchall()
        for row in rows:
            print row
        idupdate = input("Select ID to update : ")
        print "1. Update Name";
        print "2. Update Addres";
        edit = input("Select Number to Update : ")
        if(edit == 1):
        	newname = raw_input("Input New Name : ")
        	update = ("UPDATE addr SET name = %s WHERE id = %s")
        	cursorr.execute(update, (newname,idupdate))

        	connection.commit()
        elif(edit == 2):
        	newaddress = raw_input("Input New Addres : ")
        	update = ("UPDATE addr SET address = %s WHERE id = %s")
        	cursorr.execute(update, (newaddress,idupdate))

        	connection.commit()

        else:

        	print "None of the Above"

    else:

    	print "You Kill ME:("