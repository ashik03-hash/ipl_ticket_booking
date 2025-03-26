import mysql.connector
import smtplib
# make a connection
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="ashikraina",
    database="ticket_booking"
)
mycursor=mydb.cursor() 


def registration():
    id = int(input("Enter your ID - "))
    name=input("Enter your Name - ")
    mailid = input("Enter your mail - ")
    password = input("create your own password - ")
    print(f"Hi {name} your registration is completed successfully")
    sql="insert into reg_form (id , name , mailid , password) values (%s,%s,%s,%s)"
    val=(id,name,mailid,password)
    mycursor.execute(sql,val)
    mydb.commit()
    print("Your data has been stored sucessfully.............")

def login():
    name= input("Enter your username - ")
    password=input("Enter your password - ")
    sql="select * from reg_form where name=%s and password=%s"
    val=(name,password)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result:
        print(f"Hi {name} login successfull.......\n")
        print("Now you can Book your tickets and enjoy the live encounter in stadium near you ----------")
    else:
        print("Please check your username or password......")
        return login()

def login_register():
    print("**************Welcome to the online ticket booking portal***************")
    reg_log=input("Enter register for creating a new account (or) use login to continue - ")

    if reg_log == "Register":
        registration()
    elif reg_log == "Login":
        login()
    else:
        print("please select an valid option")
        return login_register()

login_register()

def chennai():
    print("******Chepauk Stadium Welcomes you*******")
    print("Select the match you want to Buy Ticket")
    print("1. CSK VS MI ")
    print("2. CSK VS RCB ")
    print("3. CSK VS KKR ")
    select_match=input("select the match you want to buy ticket - ")
    if select_match == "csk vs mi":
        print("you have selected csk vs mi match complete further steps to seal your booking------  ")
        print("Select the price range you want to purchase ticket....... \n"
        "1 - 7500Rs/-\n 2 - 5000Rs/- \n 3 - 3500Rs/- \n 4 - 2000Rs/- \n 5 - 1000Rs/-")
        select_price=input("Enter the price of the ticket you want to buy : ")
        if select_price =="balcony":
            print("You have selected balcony seat (7500 rs)----")
            print("provide the following information for seat conforming ")
            name=input("Enter your name : ")
            seat_no=int(input("Select the seat no : "))
            mailid=input("Enter your mail id : ")
            buying_price=input("Enter seat price you have buy : ")
            sql="insert into chennai_tickets (name,seat_no,mailid,buying_price) values (%s,%s,%s,%s)"
            val=(name,seat_no,mailid,buying_price)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data has been stored -------")
            print("Thank you for purchasing your data has been stored successfully\nyou will receive a confirmation mail-----")
            # sending mail to user------
            sender_mail="mohammedashik10012003@gmail.com"
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login(sender_mail,"")
            message=f"Hi {name} congratulations your Booking has been confirmed ******\n your seat number is {seat_no}"
            s.send(sender_mail,mailid,message)
            s.quit()
            print("Mail has been sended succesfully*********")

        elif select_price =="upper tier":
            print("You have selected upper Tier (5000 rs) ----")
            print("provide the following information for seat conforming ")
            name=input("Enter your name : ")
            seat_no=int(input("Select the seat no : "))
            mailid=input("Enter your mail id : ")
            buying_price=input("Enter seat price you have buy : ")
            sql="insert into chennai_tickets (name,seat_no,mailid,buying_price) values (%s,%s,%s,%s)"
            val=(name,seat_no,mailid,buying_price)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data has been stored -------")
            print("Thank you for purchasing your data has been stored successfully\nyou will receive a confirmation mail-----")
            # sending mail to user------
            sender_mail="mohammedashik10012003@gmail.com"
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login(sender_mail,"")
            message=f"Hi {name} congratulations your Booking has been confirmed ******\n your seat number is {seat_no}"
            s.send(sender_mail,mailid,message)
            s.quit()
            print("Mail has been sended succesfully*********")

        elif select_price =="lower tier":
            print("You have selected lowe tier (3500 rs) ----")
            print("provide the following information for seat conforming ")
            name=input("Enter your name : ")
            seat_no=int(input("Select the seat no : "))
            mailid=input("Enter your mail id : ")
            buying_price=input("Enter seat price you have buy : ")
            sql="insert into chennai_tickets (name,seat_no,mailid,buying_price) values (%s,%s,%s,%s)"
            val=(name,seat_no,mailid,buying_price)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data has been stored -------")
            print("Thank you for purchasing your data has been stored successfully\nyou will receive a confirmation mail-----")
            # sending mail to user------
            sender_mail="mohammedashik10012003@gmail.com"
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login(sender_mail,"")
            message=f"Hi {name} congratulations your Booking has been confirmed ******\n your seat number is {seat_no}"
            s.send(sender_mail,mailid,message)
            s.quit()
            print("Mail has been sended succesfully*********")

        elif select_price =="upper-lower stand":
            print("You have selected upper - Lower stand (2000rs)  ----")
            print("provide the following information for seat conforming ")
            name=input("Enter your name : ")
            seat_no=int(input("Select the seat no : "))
            mailid=input("Enter your mail id : ")
            buying_price=input("Enter seat price you have buy : ")
            sql="insert into chennai_tickets (name,seat_no,mailid,buying_price) values (%s,%s,%s,%s)"
            val=(name,seat_no,mailid,buying_price)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data has been stored -------")
            print("Thank you for purchasing your data has been stored successfully\nyou will receive a confirmation mail-----")
            # sending mail to user------
            sender_mail="mohammedashik10012003@gmail.com"
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login(sender_mail,"")
            message=f"Hi {name} congratulations your Booking has been confirmed ******\n your seat number is {seat_no}"
            s.send(sender_mail,mailid,message)
            s.quit()
            print("Mail has been sended succesfully*********")

        elif select_price == 5:
            print("You have selected lower stand (1000 rs) ----")
            print("provide the following information for seat conforming ")
            name=input("Enter your name : ")
            seat_no=int(input("Select the seat no : "))
            mailid=input("Enter your mail id : ")
            buying_price=input("Enter seat price you have buy : ")
            sql="insert into chennai_tickets (name,seat_no,mailid,buying_price) values (%s,%s,%s,%s)"
            val=(name,seat_no,mailid,buying_price)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data has been stored -------")
            print("Thank you for purchasing your data has been stored successfully\nyou will receive a confirmation mail-----")
            # sending mail to user------
            sender_mail="mohammedashik10012003@gmail.com"
            s=smtplib.SMTP("smtp.gmail.com",587)
            s.starttls()
            s.login(sender_mail,"")
            message=f"Hi {name} congratulations your Booking has been confirmed ******\n your seat number is {seat_no}"
            s.send(sender_mail,mailid,message)
            s.quit()
            print("Mail has been sended succesfully*********")

        else:
            print("pls select a valid option ------")
    elif select_match == "csk vs rcb":
        print("Sorry Booking for this match has been not started\n we will notify you once the booking is opens-----")
    elif select_match == "csk vs kkr":
         print("Sorry Booking for this match has been not started\n we will notify you once the booking is opens-----")

    else:
        print("Please select an valid match ----")

#def Bangalore():
#def kolkata():
def ipl_ticket_booking():

    print("-------- Welcome to IPL 2025 -------")

def ticket_booking():
    print("************Welcome to online ticket booking platform************")
    print("1 - select one for Ipl ticket booking------")
    print("2 - select Two for Pak vs Nz Ticket Booking-----")

    booking_mode=input("Enter the Category in which you need to Book Ticket")

    if booking_mode == "one":
        print("Hi You have selected IPL Ticket ")
        chennai()
    elif booking_mode == "two":
        print("sorry the match you have selected is ended..........")
    else:
        print("Select a valid option")
ticket_booking()