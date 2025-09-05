def addstudent():
	def submitadd():
		id = idval.get()
		name = nameval.get()
		mobile = mobileval.get()
		email = emailval.get()
		address = addressval.get()
		gender = genderval.get()
		dob = dobval.get()
		addedtime = time.strftime("%H:%M:%S")
		addeddate = time.strftime("%d:%m:%y")
		try:
			strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
			mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
			con.commit()
			res = messagebox.askyesnocancel('notifications','Id{} Name{} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot)
			if(res==True):
				idval.set('')
				nameval.set('')
				mobileval.set('')
				emailval.set('')
				addressval.set('')
				genderval.set('')
				dobval.set('')

		except:
			messagebox.showerror('notifications','Id already exist try another id...',parent=addroot)
		strr = "select * from studentdata1"
		mycursor.execute(strr)
		datas = mycursor.fetchall()
		studenttable.delete(*studenttable.get_children())
		for i in datas:
			vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
			studenttable.insert('',END,values=vv)
	################################################################# Add student Labels
	addroot = Toplevel(master=DataEntryFrame)
	addroot.grab_set()
	addroot.geometry("470x540+220+200")
	addroot.title('Student Management System')
	addroot.config(bg='firebrick1')
	addroot.iconbitmap("manager.ico")
	addroot.resizable(False,False)
	idlabel =Label(addroot,text="Enter Id:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	idlabel.place(x=10,y=10)
	
	namelabel =Label(addroot,text="Enter Name:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel =Label(addroot,text="Enter Mobile:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel =Label(addroot,text="Enter Email:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	emaillabel.place(x=10,y=190)

	Addresslabel =Label(addroot,text="Enter Address:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	Addresslabel.place(x=10,y=250)

	genderlabel =Label(addroot,text="Enter Gender:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel =Label(addroot,text="Enter D.O.B:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	doblabel.place(x=10,y=370)
	#############################################################Add student enteries
	idval = StringVar()
	nameval = StringVar()
	mobileval = StringVar()
	emailval = StringVar()
	addressval = StringVar()
	genderval = StringVar()
	dobval = StringVar()


	identry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=idval)
	identry.place(x=230,y=10)
	
	nameentry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=nameval)
	nameentry.place(x=230,y=70)
	
	mobileentry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=mobileval)
	mobileentry.place(x=230,y=130)
	
	emailentry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=emailval)
	emailentry.place(x=230,y=190)
	
	addressentry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=addressval)
	addressentry.place(x=230,y=250)
	
	genderentry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=genderval)
	genderentry.place(x=230,y=310)
	
	dobentry = Entry(addroot,font=("times",15,"bold"),bd=5,textvariable=dobval)
	dobentry.place(x=230,y=370)
	#################################################add button
	submitbtn = Button(addroot,text="Submit",font=('times',15,'bold'),width=20,bd=5,activebackground='springgreen2',activeforeground='white',
						bg='red',command=submitadd)
	submitbtn.place(x=100,y=420)

	addroot.mainloop()
def searchstudent():
	def search():
		id = idval.get()
		name = nameval.get()
		mobile = mobileval.get()
		email = emailval.get()
		address = addressval.get()
		gender = genderval.get()
		dob = dobval.get()
		addeddate = time.strftime("%d:%m:%y")
		if(id != ""):
			strr = 'select * from studentdata1 where id=%s'
			mycursor.execute(strr,(id))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(name != ""):
			strr = 'select * from studentdata1 where name=%s'
			mycursor.execute(strr,(name))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(mobile != ""):
			strr = 'select * from studentdata1 where mobile=%s'
			mycursor.execute(strr,(mobile))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(email != ""):
			strr = 'select * from studentdata1 where email=%s'
			mycursor.execute(strr,(email))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(address != ""):
			strr = 'select * from studentdata1 where address=%s'
			mycursor.execute(strr,(address))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(gender != ""):
			strr = 'select * from studentdata1 where gender=%s'
			mycursor.execute(strr,(gender))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(dob != ""):
			strr = 'select * from studentdata1 where dob=%s'
			mycursor.execute(strr,(dob))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

		elif(addeddate != ""):
			strr = 'select * from studentdata1 where addeddate=%s'
			mycursor.execute(strr,(addeddate))
			datas = mycursor.fetchall()
			studenttable.delete(*studenttable.get_children())
			for i in datas:
				vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
				studenttable.insert('',END,values=vv)

	searchroot = Toplevel(master=DataEntryFrame)
	searchroot.grab_set()
	searchroot.geometry("470x540+220+200")
	searchroot.title('Student Management System')
	searchroot.config(bg='firebrick1')
	searchroot.iconbitmap("manager.ico")
	searchroot.resizable(False,False)
	################################################################# Add student Labels
	idlabel =Label(searchroot,text="Enter Id:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	idlabel.place(x=10,y=10)
	namelabel =Label(searchroot,text="Enter Name:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel =Label(searchroot,text="Enter Mobile:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel =Label(searchroot,text="Enter Email:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	emaillabel.place(x=10,y=190)

	Addresslabel =Label(searchroot,text="Enter Address:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	Addresslabel.place(x=10,y=250)

	genderlabel =Label(searchroot,text="Enter Gender:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel =Label(searchroot,text="Enter D.O.B:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	doblabel.place(x=10,y=370)

	datelabel =Label(searchroot,text="Enter Date:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	datelabel.place(x=10,y=430)
	#############################################################Add student enteries
	idval = StringVar()
	nameval = StringVar()
	mobileval = StringVar()
	emailval = StringVar()
	addressval = StringVar()
	genderval = StringVar()
	dobval = StringVar()
	dateval = StringVar()


	identry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=idval)
	identry.place(x=230,y=10)
	
	nameentry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=nameval)
	nameentry.place(x=230,y=70)
	
	mobileentry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=mobileval)
	mobileentry.place(x=230,y=130)
	
	emailentry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=emailval)
	emailentry.place(x=230,y=190)
	
	addressentry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=addressval)
	addressentry.place(x=230,y=250)
	
	genderentry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=genderval)
	genderentry.place(x=230,y=310)
	
	dobentry = Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=dobval)
	dobentry.place(x=230,y=370)

	dateentry= Entry(searchroot,font=("times",15,"bold"),bd=5,textvariable=dateval)
	dateentry.place(x=230,y=430)
	#################################################add button
	submitbtn = Button(searchroot,text="Search",font=('times',15,'bold'),width=20,bd=5,activebackground='green2',activeforeground='white',
						bg='springgreen2',command=search)
	submitbtn.place(x=100,y=490)

	searchroot.mainloop()

	print("student search")
def deletestudent():
	cc = studenttable.focus()
	content = studenttable.item(cc)
	pp = content['values'][0]
	strr = 'delete from studentdata1 where id=%s'
	mycursor.execute(strr,(pp))
	con.commit()
	messagebox.showinfo('notifications','Id{} deleteed sucessfully....'.format(pp))
	strr = 'select * from studentdata1'
	mycursor.execute(strr)
	datas = mycursor.fetchall()
	studenttable.delete(*studenttable.get_children())
	for i in datas:
		vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
		studenttable.insert('',END,values=vv)

	
def updatestudent():
	def update():
		id = idval.get()
		name = nameval.get()
		mobile = mobileval.get()
		email = emailval.get()
		address = addressval.get()
		gender = genderval.get()
		dob = dobval.get()
		addeddate = dateval.get()
		time = timeval.get()

		strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,addeddate=%s,time=%s where id=%s'
		mycursor.execute(strr,(name,mobile,email,address,gender,dob,addeddate,time,id))
		con.commit()
		messagebox.showinfo('notifications',"Id{} Modified sucessfully....".format(id),parent=updateroot)
		strr = 'select * from studentdata1'
		mycursor.execute(strr)
		datas = mycursor.fetchall()
		studenttable.delete(*studenttable.get_children())
		for i in datas:
			vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
			studenttable.insert('',END,values=vv)

	updateroot = Toplevel(master=DataEntryFrame)
	updateroot.grab_set()
	updateroot.geometry("470x640+220+200")
	updateroot.title('Student Management System')
	updateroot.config(bg='firebrick1')
	updateroot.iconbitmap("manager.ico")
	updateroot.resizable(False,False)
	################################################################# Add student Labels
	idlabel =Label(updateroot,text="Enter Id:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	idlabel.place(x=10,y=10)
	
	namelabel =Label(updateroot,text="Enter Name:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	namelabel.place(x=10,y=70)

	mobilelabel =Label(updateroot,text="Enter Mobile:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	mobilelabel.place(x=10,y=130)

	emaillabel =Label(updateroot,text="Enter Email:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	emaillabel.place(x=10,y=190)

	Addresslabel =Label(updateroot,text="Enter Address:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	Addresslabel.place(x=10,y=250)

	genderlabel =Label(updateroot,text="Enter Gender:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	genderlabel.place(x=10,y=310)

	doblabel =Label(updateroot,text="Enter D.O.B:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	doblabel.place(x=10,y=370)

	datelabel =Label(updateroot,text="Enter Date:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	datelabel.place(x=10,y=430)

	timelabel =Label(updateroot,text="Enter Time:",bg="cyan",font=("times",20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	timelabel.place(x=10,y=490)
	#############################################################Add student enteries
	idval = StringVar()
	nameval = StringVar()
	mobileval = StringVar()
	emailval = StringVar()
	addressval = StringVar()
	genderval = StringVar()
	dobval = StringVar()
	dateval = StringVar()
	timeval = StringVar()


	identry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=idval)
	identry.place(x=230,y=10)
	
	nameentry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=nameval)
	nameentry.place(x=230,y=70)
	
	mobileentry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=mobileval)
	mobileentry.place(x=230,y=130)
	
	emailentry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=emailval)
	emailentry.place(x=230,y=190)
	
	addressentry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=addressval)
	addressentry.place(x=230,y=250)
	
	genderentry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=genderval)
	genderentry.place(x=230,y=310)
	
	dobentry = Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=dobval)
	dobentry.place(x=230,y=370)

	dateentry= Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=dateval)
	dateentry.place(x=230,y=430)

	timeentry= Entry(updateroot,font=("times",15,"bold"),bd=5,textvariable=timeval)
	timeentry.place(x=230,y=490)
	#################################################add button
	submitbtn = Button(updateroot,text="Update",font=('times',15,'bold'),width=20,bd=5,activebackground='green2',activeforeground='white',
						bg='springgreen2',command=update)
	submitbtn.place(x=100,y=550)
	cc = studenttable.focus()
	content = studenttable.item(cc)
	pp = content['values']
	if(len(pp)!=0):
		idval.set(pp[0])
		nameval.set(pp[1])
		mobileval.set(pp[2])
		emailval.set(pp[3])
		addressval.set(pp[4])
		genderval.set(pp[5])
		dobval.set(pp[6])
		dateval.set(pp[7])
		timeval.set(pp[8])


	updateroot.mainloop()
	print("student update")
def showstudent():
		strr = 'select * from studentdata1'
		mycursor.execute(strr)
		datas = mycursor.fetchall()
		studenttable.delete(*studenttable.get_children())
		for i in datas:
			vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
			studenttable.insert('',END,values=vv)
def exportstudent():
	ff = filedialog.asksaveasfilename()
	gg = studenttable.get_children()
	id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
	for i in gg:
		content = studenttable.item(i)
		pp = content['values']
		id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
		dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
	dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Addeddate','Addedtime']
	df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
	paths = r'{}.csv'.format(ff)
	df.to_csv(paths,index=False)
	messagebox.showinfo('notifications',"Student data is sucessfully saved.....".format(paths))


def exitstudent():
	res = messagebox.askyesnocancel("notification","Do you want to exit?")
	if(res==True):
		root.destroy()
###########################################################################################connection of database
def connectdb():
	def submitdb():
		global con,mycursor
		host = hostval.get()
		user = userval.get()
		password = passwordval.get()
		# host = 'localhost'
		# user = 'root'
		# password = '2002'
		try:
			con =pymysql.connect(host=host,user=user,password=password)
			mycursor = con.cursor()
		except:
			messagebox.showerror('notification','Data is incorrect please try again')
			return
		try:
			strr = 'create database studentmanagementsystem1'
			mycursor.execute(strr)
			strr = 'use studentmanagementsystem1'
			mycursor.execute(strr)
			strr = 'create table studentdata1(id int(11),name varchar(25),Mobile varchar(12),Email varchar(50),Address varchar(100),gender varchar(10),dob varchar(25),addeddate varchar(25),time varchar(25))'
			mycursor.execute(strr)

			strr = 'alter table studentdata1 modify column id int not null'
			mycursor.execute(strr)
			strr = 'alter table studentdata1 modify column id int primary key'
			mycursor.execute(strr)	
			messagebox.showinfo('notification','Database Created and Now You are connected to the database.....',parent=dbroot)


		except:
			strr="use studentmanagementsystem1"
			mycursor.execute(strr)
			messagebox.showinfo('notification','Now You are connected to the database.....',parent=dbroot)
		dbroot.destroy()



	dbroot = Toplevel()
	dbroot.grab_set()
	dbroot.geometry("470x250+800+230")
	dbroot.iconbitmap("manager.ico")
	dbroot.resizable(False,False)
	dbroot.config(bg="bisque2")
	##################################### connectdb Labels
	hostlabel = Label(dbroot,text="Enter host : ",bg="cyan",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	hostlabel.place(x=10,y=10)

	userlabel = Label(dbroot,text="Enter user : ",bg="cyan",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor='w')
	userlabel.place(x=10,y=70)

	passwordlabel = Label(dbroot,text="Enter password : ",bg="cyan",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=13,anchor='w')
	passwordlabel.place(x=10,y=130)

############################################connectdb Entry
	hostval = StringVar()
	userval = StringVar()
	passwordval = StringVar()

	hostentry = Entry(dbroot,font=("times",15,"bold"),bd=5,textvariable=hostval)
	hostentry.place(x=250,y=10)

	userentry = Entry(dbroot,font=("times",15,"bold"),bd=5,textvariable=userval)
	userentry.place(x=250,y=70)

	passwordentry = Entry(dbroot,font=("times",15,"bold"),bd=5,textvariable=passwordval)
	passwordentry.place(x=250,y=130)

######################################################### connectdb button
	submitbutton = Button(dbroot,text="Submit",font=("times",15,"bold"),width=20,bg="medium purple",activebackground="Purple",activeforeground="white",bd=5,command=submitdb)
	submitbutton.place(x=100,y=190)
	dbroot.mainloop()




###################################################
def tick():
	time_string = time.strftime("%H:%M:%S")
	date_string = time.strftime("%d/%m/%y")
	clock.config(text="Date :"+date_string+ "\n" +"Time :"+time_string)
	clock.after(200,tick)
################################################################################### Intro slider
import random
colors = ["red","yellow","green","springgreen2","pink","red2","cyan"]
def IntroLabelColorTick():
	fg = random.choice(colors)
	SliderLabel.config(fg=fg)
	SliderLabel.after(2,IntroLabelColorTick)

def IntroLabelTick():
	global count,text
	if(count>=len(ss)):
		count = 0
		text = ""
		SliderLabel.config(text=text)
	else:
		text = text+ss[count]
		SliderLabel.config(text=text)
		count+=1
	SliderLabel.after(100,IntroLabelTick)
###############################################################################################################
from tkinter import*
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas 
import pymysql
import time
root =Tk()
root.title("Student Management System")
root.config(bg="cyan")
root.geometry("1174x700+200+50")
root.iconbitmap("manager.ico")
root.resizable(False,False)
################################################################################################################ frames
#########################################################################data entry frame intro

DataEntryFrame = Frame(root,bg="cyan",relief=GROOVE,bd=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text="---------------Welcome--------------",width=30,font=("Algerian",22,"bold","italic"),bg='cyan',fg="orange")
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text="1. Add student",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text="2. search student ",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text="3. delete student",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text="4. update student",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text="5. show student",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text="6. Export Data",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text="7. Exit",width=15,font=("Algerian",20,"bold"),bd=5,bg='indianred1',activebackground="springgreen2",relief=RIDGE,
				activeforeground="white",command=exitstudent)
exitbtn.pack(side=TOP,expand=True)
#########################################################################show data frame
ShowDataFrame = Frame(root,bg="cyan",relief=GROOVE,bd=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

#############################################################showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=("Algerian",20,'bold'),foreground='springgreen2')
style.configure('Treeview',font=("times",15,'bold'),foreground='black',background='cyan')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,column=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
						yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command= studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=500)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=200)
studenttable.column('Added Date',width=200)
studenttable.column('Added Time',width=200)
studenttable.pack(fill=BOTH,expand=1)


############################################################################################################### slider
ss = "Welcome To Student Management System"
count = 0
text = ""
#############################################
SliderLabel =Label(root,text=ss,font=("Algerian",20,"italic","bold"),relief=RIDGE,bd=4,width=35,bg="PaleVioletRed2")
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
############################################################################################################### clock
clock = Label(root,font=("times",14,"bold"),relief=RIDGE,bd=4,bg="cornsilk2")
clock.place(x=0,y=0)
tick()
############################################################################################################### connect to database
connectbutton = Button(root,text="Connect To Database",width=20,font=("Algerian",13,"italic","bold"),relief=RIDGE,borderwidth=5,bg="papaya whip",
				activebackground="Peach puff",activeforeground="white",command=connectdb)
connectbutton.place(x=938,y=0)


root.mainloop()

