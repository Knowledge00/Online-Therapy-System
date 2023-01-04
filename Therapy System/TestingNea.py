from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import *
import sqlite3
from subprocess import call
from winotify import Notification
import datetime
from datetime import date

                                            # IF YOU WANT TO RUN USE THE CHAT FUNCTION YOU WILL NEED TO RUN THE "server.py" FILE, IT WILL BE IN THE FOLDER
black = "#000000"
white = "#FFFFFF"
blue = "#32A6CC"
pink = "#CE0279"
purple = "#664193"
root = Tk()
root.withdraw()
class Design():
    def __init__(self,Window_Name): 
        Window_Name.resizable(0,0) # Tab cant be enlarged or minimised
        Window_Name.borderwidth=0 # removes the boarder
        Window_Name.wm_attributes("-transparentcolor", "#000004") # allows the tab to be curved, by making it transparent for when the colour is hex "#000004"
        Window_Name.geometry("1000x650+100+100") # Dimension of Tab and positioning on the screen
        Window_Name.title("MindServe") # Sets Tab name to "MindServe"
    def Pictures(self):
        self.FindB = PhotoImage(file ="Find.png") # ButtonOverlay that says "Find"
        self.Xpic = PhotoImage(file = "X.png") # ButtonOverlay that says "X" - closes the tab
        self.APic = PhotoImage(file = "Arrow.png") # Back Arrow ButtonOverlay - goes to the previous interface
        self.WelcomePage = PhotoImage(file = "WelcomePage.png") # PageOverlay for the SignIn Page
        self.SignInB = PhotoImage(file = "SignInB.png") # 
        self.SignUP = PhotoImage(file = "SignUP.png")
        self.MainC = PhotoImage(file = "MainC.png")
        self.Calendar_M = PhotoImage(file = "Calendar.png")
        self.ConditionP = PhotoImage(file = "Condition.png") 
        self.SymptomT_M = PhotoImage(file = "Symptom.png")# 
        self.SymptomT_B = PhotoImage(file ="STB.png")
        self.MedicationTphoto = PhotoImage(file ="MTB.png")
        self.Calendarphoto = PhotoImage(file ="CB.png")
        self.Journal_B = PhotoImage(file ="JB.png")
        self.CG_B = PhotoImage(file ="CG_B.png")
        self.Settings_B = PhotoImage(file ="SettingB.png")
        self.Remove_B = PhotoImage(file = "Remove_B.png")
        self.Edit_B = PhotoImage(file = "Edit_B.png")
        self.Medication_M = PhotoImage(file = "MTM.png")
        self.Add_B = PhotoImage(file = "Add_B.png")
        self.AddMarker_B = PhotoImage(file = "AddMarkerB.png")
        self.Therapist_R = PhotoImage(file = "TheraR.png")
        self.Caccount_B = PhotoImage(file = "CA.png")
        self.Choice_M = PhotoImage(file = "Choice.png")
        self.Therapist_B = PhotoImage(file ="TherB.png")
        self.Client_B = PhotoImage(file ="ClientB.png")
        self.Client_R = PhotoImage(file = "RegClient.png")
        self.Medication_Add_M = PhotoImage(file = "Medication_Add_M.png")
        self.Medication_Remove_M = PhotoImage(file = "Medication_Remove_M.png")
        self.MyTherapist_B = PhotoImage(file = "MyTherapistB.png")
        self.SurveyP = PhotoImage(file = "Survey.png")
        self.OfferP = PhotoImage(file = "Offer.png")
        self.AcceptB = PhotoImage(file = "Accept.png")
        self.DeclineB = PhotoImage(file = "Decline.png")
        self.MyTherapist_M = PhotoImage(file = "MyTherapist.png")
        self.RemoveB = PhotoImage(file = "Remove.png")
        self.RateB = PhotoImage(file = "Rate.png")
        self.Chat = PhotoImage(file = "ChatB.png")
        self.AddB = PhotoImage(file = "AddTherapist.png")
        self.SaveB = PhotoImage(file = "SaveB.png")
        self.ViewB = PhotoImage(file = "View.png")
        self.NextB = PhotoImage(file = "NextB.png")
        self.JournalM = PhotoImage(file = "Journal.png")
        self.Therapist_M = PhotoImage(file = "TherapistP.png")
        self.Clients_B = PhotoImage(file = "ClientsB.png")
        self.MyAccount_B = PhotoImage(file = "MyAccountB.png")

    def Close(self):
        self.destroy()
    def Database(self):
        self.data = sqlite3.connect('NEA.A.db')
        self.cur =self.data.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS LoginDetails (
            	    "UserID"	INTEGER,
                    "First_Name"	text,
                    "Last_Name"	text,
                    "Password"	TEXT,
                    "Phone_Number"	text,
                    "profession"	text,
                    "Email"	text,
                    "DateOfBirth" Numeric,
                    PRIMARY KEY("UserID" AUTOINCREMENT)
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS SymptomT (
                    "UserID" INTEGER,
                    "Date" NUMERIC,
                    "Rating" INTEGER,
                    FOREIGN KEY("UserID") REFERENCES "LoginDetails"("UserID")
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS MedicationT (
                    "UserID" INTEGER,
                    "Name" TEXT,
                    "Quantity" INTEGER,
                    "Times" INTEGER,
                    FOREIGN KEY("UserID") REFERENCES "LoginDetails"("UserID")
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS CalendarT (
                    "UserID" INTEGER,
                    "Date" NUMERIC,
                    "Note" TEXT,
                    FOREIGN KEY("UserID") REFERENCES "LoginDetails"("UserID")
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS JournalT (
                    "UserID" INTEGER,
                    "Name" TEXT,
                    "Text" TEXT,
                    FOREIGN KEY("UserID") REFERENCES "LoginDetails"("UserID")
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS TherapistProfile (
                    "UserID" INTEGER,
                    "Rating" INTEGER,
                    "TotalClients" INTEGER,
                    "CurrentClients" INTEGER,
                    FOREIGN KEY("UserID") REFERENCES "LoginDetails"("UserID")
                    )''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS TherapistClients (
                    "UserID" INTEGER,
                    "ClientID" INTEGER,
                    FOREIGN KEY("UserID") REFERENCES "LoginDetails"("UserID")
                    )''')
        self.data.commit()
        self.data.close()



class Window(Design): # First window the user will see (Login and Sign Up)
    def __init__(self):
        self.EmailB = StringVar()
        self.PasswordB = StringVar()
        self.message = StringVar()
        self.result= StringVar()
        self.F_name = StringVar()
        self.L_name = StringVar()
        self.Pass = StringVar()
        self.Email = StringVar()
        self.Phone = StringVar()
        self.clicked = StringVar()
        self.CPass = StringVar()
    def main(self):
        self.Starting = Toplevel()
        super().__init__(self.Starting)#inheriting the initialise method in design so that all the window sizes are consistense and each window has the curved borders
        super().Pictures()#  inheriting the Picture method from the "Design" Class
        Label(self.Starting,image = self.WelcomePage, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
        Label(self.Starting, text="",textvariable=self.message,fg=black,bg = "#473DF8",font=("Arial",12, "bold")).place(x=455,y=400)
        Entry(self.Starting,textvariable = self.EmailB,bd = 0, width = 31, font = "Arial 14").place(x=455, y=225)
        Entry(self.Starting,textvariable = self.PasswordB,bd = 0,show="*", width = 31, font = "Arial 14").place(x=455, y= 330)
        Button(self.Starting,image = self.SignInB,activebackground=white, bd =0,command = self.SignIn).place(width = 92, height = 41,x=601, y=456)
        Button(self.Starting,image = self.SignUP,bg = black,activebackground=black, bd =0,command = lambda:[(self.Starting).destroy(), self.User()]).place(x=74, y=402)
        Button(self.Starting,image = self.Xpic,bd=0,bg="#4E40F9", activebackground="#4E40F9", command = root.destroy).place(x=908, y=16)
    def SignIn(self):
        self.Email = self.EmailB.get()
        self.Password = self.PasswordB.get()
        self.ClientRole = "Client"
        if self.Email == "" or self.Password == "": # exception handling - Gives an error message if 1 or both entry boxes are left empty
            self.message.set("One or Both Entries have been left Empty!") # error message
        else:
            self.data = sqlite3.connect("NEA.A.db")
            self.cur = self.data.cursor() 
            self.cur.execute('SELECT UserID from LoginDetails where Email="%s" and Password="%s"'%(self.Email,self.Password)); # searches for the data within the table ("users") where the user input for the email and password match a record
            if self.cur.fetchone():#if it has found a match then do ↓
                self.UserID = self.cur.fetchone()
                self.additional = self.cur.execute('SELECT * from LoginDetails where Email="%s" and Password="%s" and profession= "%s"'%(self.Email,self.Password, self.ClientRole));# now its searching for that same record but if it has the "client profession"
                if self.additional.fetchone(): # if it has found a match then it will do the following ↓
                    self.UserID = self.cur.execute('SELECT UserID from LoginDetails where Email="%s" and Password="%s"'%(self.Email,self.Password));
                    self.help =self.UserID.fetchone()
                    self.result, = self.help
                    self.Main_to_CP(self.result)
                    self.collection = self.cur.execute('''SELECT Name, Quantity,Times FROM MedicationT WHERE UserID = "%s"'''%(self.result))
                    for i in self.collection:
                        self.message = "Medicine: %s\nQuantity: %s\nTimes per day: %s"%(i[0],i[1],i[2])
                        Notif = Notification(app_id="MindServe - Medication Update", # The sendings notifications when the user signs, regarding users taking their daily medication
                                        title = "Reminder",
                                        msg = self.message,
                                        icon =r"C:\NeaA\Logo.png")
                        Notif.show()
                else:
                    self.Main_to_TP(self.UserID)
            else: # if it hasnt found a record that didnt match the email and password then it will display ↓
                self.message.set("Wrong username or password!!!")   
        return self.result
    def Main_to_CP(self,something):# Composition
        self.ClientPage = ClientP() 
        self.ClientPage.mainCP(something)
    def Main_to_TP(self,something):
        self.TherapistPage = TherapistP()
        self.TherapistPage.MainTP(something)
    def Submit(self,F_name,L_name,Pass,Phone,clicked,Email,DOB):
        self.data = sqlite3.connect('NEA.A.db')
        self.cur = self.data.cursor()
        self.cur.execute("INSERT INTO LoginDetails VALUES (NULL,:First_Name, :Last_name, :Password,:Phone_Number,:profession,:Email,:DateOfBirth)",
                            {
                            "First_Name": F_name.get(),
                            "Last_name": L_name.get(),
                            "Password": Pass.get(),
                            "Phone_Number": Phone.get(),
                            "profession": clicked.get(),
                            "Email": Email.get(),
                            "DateOfBirth": DOB.get()
                            }
                        )
        self.data.commit()
        self.data.close()

    def User(self): 
        self.UW = Toplevel()
        super(Window,self).__init__(self.UW)
        Label(self.UW, image = self.Choice_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
        Button(self.UW, image = self.Therapist_B,bd=0, bg =black,activebackground=black,command = lambda:[(self.UW).destroy(),self.TherSignUp()]).place(x= 95, y= 230)
        Button(self.UW, image = self.Client_B,bd=0, bg =black,activebackground=black, command = lambda:[(self.UW).destroy(),self.CustSignUp()]).place(x= 568, y =230)
        Button(self.UW,image = self.Xpic,bd=0,bg=black, activebackground=black, command = (self.UW).destroy ).place(x=910, y=16)
        Button(self.UW, image = self.APic,bg =black,bd= 0,activebackground=black, command =lambda:[(self.UW).destroy(),self.main()]).place(x=35,y=16)
    def CustSignUp(self):
        self.CSUW = Toplevel()
        super(Window,self).__init__(self.CSUW)
        Label(self.CSUW, image = self.Client_R, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
        Button(self.CSUW,image = self.Xpic,bd=0,bg=black, activebackground=black, command = self.CSUW.destroy ).place(x=910, y=16)
        Button(self.CSUW, image = self.APic,bg =black,bd= 0,activebackground=black, command =lambda:[self.CSUW.destroy(),self.User()]).place(x=35,y=16)
        Entry(self.CSUW,textvariable = self.F_name,width = 21,bd =0, font = "Arial 15").place(x=122,y=230)
        Entry(self.CSUW,width = 21,textvariable = self.L_name,bd =0, font = "Arial 15").place(x=539,y=230)
        Entry(self.CSUW,width = 21,bd =0,textvariable = self.Email, font = "Arial 15").place(x=122,y=328)
        Entry(self.CSUW,width = 21,bd =0,textvariable=self.Phone, font = "Arial 15").place(x=122,y=419)
        Entry(self.CSUW,width = 21,bd =0,textvariable=self.Pass, font = "Arial 15").place(x=378,y=305)
        Entry(self.CSUW,width = 21,bd =0,textvariable=self.CPass, font = "Arial 15").place(x=539, y=419)
        sel = StringVar()
        self.clicked = StringVar()
        self.clicked.set("Client")
        self.DOB = DateEntry(self.CSUW,selectmode='day',date_pattern='dd/MM/yyyy', textvariable = sel)
        self.DOB.pack()
        Button(self.CSUW, image = self.Caccount_B, bd = 0, bg = black,activebackground=black, command = lambda:[self.main(),self.Submit(self.F_name,self.L_name,self.Pass,self.Phone,self.clicked,self.Email,self.DOB), self.CSUW.destroy()]).place(x= 113,y=519)
    def TherSignUp(self):
        self.TSUW = Toplevel()
        super(Window,self).__init__(self.TSUW)
        Label(self.TSUW, image = self.Therapist_R, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
        Button(self.TSUW,image = self.Xpic,bd=0,bg=black, activebackground=black, command = self.TSUW.destroy).place(x=910, y=16)
        Entry(self.TSUW,textvariable = self.F_name,width = 21,bd =0, font = "Arial 15").place(x=70,y=195)
        Entry(self.TSUW,width = 21,textvariable = self.L_name,bd =0, font = "Arial 15").place(x=378, y=195)
        Entry(self.TSUW,width = 21,bd =0,textvariable = self.Email, font = "Arial 15").place(x=676, y=195)
        Entry(self.TSUW,width = 21,bd =0,textvariable=self.Phone, font = "Arial 15").place(x=70, y=305)
        Entry(self.TSUW,width = 21,bd =0,textvariable=self.Pass, font = "Arial 15").place(x=378,y=305)
        Entry(self.TSUW,width = 21,bd =0,textvariable=self.CPass, font = "Arial 15").place(x=676,y=305)
        self.clicked.set("Field of work")
        Job = ["marriage and family counselor", "addiction therapist", "behavioural therapist",
            "cognitive/cbt therapist", "eating disorder therapist",
                "youth therapist (ages 10-21)",
            "trauma therapist", "social therapist"]
        self.DOB = DateEntry(self.TSUW,selectmode='day',date_pattern='dd/MM/yyyy')
        self.DOB.pack()
        self.Prof = OptionMenu(self.TSUW,self.clicked ,*Job)
        s=ttk.Style()
        s.theme_use("clam")
        self.Prof["highlightthickness"]=0
        self.Prof["borderwidth"] = 0
        self.Prof["bg"] = white
        self.Prof["activebackground"] = white
        self.Prof.config(width=23)
        self.Prof.config(font = "Arial 12")
        self.Prof.place(x=378,y=412)
        Button(self.TSUW, image = self.APic,bg =black,bd= 0,activebackground=black, command =lambda:[(self.TSUW).destroy(), self.User()]).place(x=35,y=16)
        Button(self.TSUW, image = self.Caccount_B,bg =black,bd= 0,activebackground=black,command =lambda:[self.Submit(self.F_name,self.L_name,self.Pass,self.Phone,self.clicked,self.Email,self.DOB),(self.TSUW).destroy(),self.main()]).place(x=115, y= 480)
class ClientP(Window):
        def __init__(self):
            self.ClientP = Toplevel()
            super(Window, self).__init__(self.ClientP)
            super(Window, self).Pictures()
            self.MedicineName = StringVar()
            self.Quantity = IntVar()
            self.Times = IntVar()
            self.DropChoice = StringVar()
            self.message = StringVar()
            s=ttk.Style()
            s.theme_use("clam")

        def mainCP(self,value):
            self.NumberID = value
            Label(self.ClientP, image = self.MainC, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.ClientP, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
            Button(self.ClientP, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[self.ClientP.destroy(),self.MainP()]).place(x=39, y=21)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.SymptomT_B, bg="black", command = lambda:[self.ClientP.destroy(), self.SymptomT_Window(self.NumberID)]).place(x= 82, y=174)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.MedicationTphoto, bg="black", command = lambda:[self.ClientP.destroy(),self.MedicationT_Window()]).place(x= 82, y=269)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.Calendarphoto, bg="black", command = lambda:[self.ClientP.destroy(),self.Calendar_Window()]).place(x= 82, y=364)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.Journal_B, bg="black", command = lambda:[self.ClientP.destroy(),self.Journal_Window()]).place(x= 756, y=269)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.CG_B, bg="black", command = lambda:[self.ClientP.destroy(),self.Condition_Window()]).place(x= 756, y=174)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.Settings_B, bg="black", command = lambda:[self.ClientP.destroy(),self.Settings_Window()]).place(x= 756, y=364)
            Button(self.ClientP,width = 178, height = 84,bd=0, activebackground=black , image = self.MyTherapist_B, bg="black", command = lambda:[self.ClientP.destroy(),self.MyTherapist_Window()]).place(x= 411, y=554)
            
        def SymptomT_Window(self,value):
            self.change = str(value)
            call(["python", "SymptomTracker.py",self.change])
        def MedicationT_Window(self):
            self.MTW = Toplevel()
            super(Window,self).__init__(self.MTW)
            Label(self.MTW,image = self.Medication_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.MTW, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
            Button(self.MTW, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[(self.MTW).destroy(),self.Go_Back(self.NumberID)]).place(x=39, y=21)
            Button(self.MTW, image = self.Add_B,activebackground=black,bd=0,bg="black", command = self.Add_W).place(x=218,y=556)
            Button(self.MTW, image = self.Remove_B,activebackground=black,bd=0,bg="black", command = self.Remove_W).place(x=572,y=556)
            self.data = sqlite3.connect("NEA.A.db")
            self.cur = self.data.cursor()
            self.collection = self.cur.execute('''SELECT Name, Quantity,Times FROM MedicationT WHERE UserID = "%s"'''%(self.NumberID))
            self.list = self.collection.fetchall()
            for i in range(len(self.list)):
                for j in range(0,3):
                    Label(self.MTW,text=self.list[i][j], font = ("Times",15), fg= white,bg= black).place(x=129+(300*j),y=280+(50*i))
        def Remove_W(self):
            self.Remove_Window = Toplevel()
            super(Window,self).__init__(self.Remove_Window)
            self.Remove_Window.geometry("650x830+100+100")
            Label(self.Remove_Window,image = self.Medication_Remove_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            self.data = sqlite3.connect('NEA.A.db')
            self.cur = self.data.cursor()
            self.ProfList = self.cur.execute('''SELECT DISTINCT Name
                                                 FROM MedicationT
                                                 Where UserID = "%s"'''%(self.NumberID));
            my_list = [r for r, in self.ProfList]
            self.Choice=OptionMenu(self.Remove_Window,self.DropChoice,*my_list)
            Button(self.Remove_Window,command =lambda:[self.Remove(self.DropChoice.get())]).place(x=218,y=520)
            self.Choice["highlightthickness"]=0
            self.Choice["borderwidth"] = 0
            self.Choice["bg"] = blue
            self.Choice["activebackground"] = blue
            self.Choice.config(width=23)
            self.Choice.config(font = "Arial 12")
            self.Choice.place(x=172,y=327)
        def Remove(self,option):
            self.data = sqlite3.connect('NEA.A.db')
            self.cur = self.data.cursor()
            self.cur.execute('''DELETE FROM MedicationT WHERE UserID = "%s" and Name = "%s"'''%(self.NumberID,option))
            self.data.commit()
            self.data.close()
            self.Remove_Window.destroy()
            self.MTW.destroy()
            self.MedicationT_Window()

        def Chat_W(self):
            call(["python", "Chat.py"])
              

        def Add_W(self):
            self.Add_Window = Toplevel()
            super(Window,self).__init__(self.Add_Window)
            self.Add_Window.geometry("650x830+100+100")
            Label(self.Add_Window,image = self.Medication_Add_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Entry(self.Add_Window,textvariable=self.MedicineName).place(x=273,y=318)
            Entry(self.Add_Window,textvariable=self.Quantity).place(x=273,y=393)
            Entry(self.Add_Window,textvariable=self.Times).place(x=273,y=468)
            Button(self.Add_Window, image=self.Add_B, bd=0,bg=black, activebackground= black, command = self.Add).place(x=233,y=636)
        def Add(self):
            Label(self.Add_Window, textvariable=self.message, text = "").place(x=60,y=60)
            try:
                if type(self.Quantity.get()) == int and type(self.Times.get()) == int:
                    self.cur = self.data.cursor()
                    self.Checking = self.cur.execute('''SELECT Name FROM MedicationT WHERE UserID = "%s" and Name = "%s"'''%(self.NumberID, self.MedicineName.get()))

                    if self.Checking.fetchone():
                        self.confirm = Toplevel() 
                        Button(self.confirm, text= "yes", command = lambda:[self.confirm.destroy(),self.overwrite()]).pack()
                        Button(self.confirm, text= "no", command = lambda:[self.confirm.destroy()]).pack()
                    else:
                        self.cur.execute('''INSERT INTO MedicationT(UserID,Name,Quantity,Times) VALUES ("%s","%s","%s","%s")'''%(self.NumberID,self.MedicineName.get(),self.Quantity.get(),self.Times.get()))
                        self.data.commit()
                else:
                    self.message.set("Invalid Input(s)")
            except:
                self.message.set("Invalid Input(s)")

        def overwrite(self):
            self.cur.execute('''UPDATE MedicationT SET Quantity = "%s", Times = "%s" WHERE UserID = "%s" and Name = "%s"'''%(self.Quantity.get(),self.Times.get(),self.NumberID,self.MedicineName.get()))
            self.data.commit()
            self.Add_Window.destroy()
            self.MTW.destroy()
            self.MedicationT_Window()



        def Go_Back(self,value):
            Back = ClientP()    
            Back.mainCP(value)


        def Calendar_Window(self):
            self.CalendarW = Toplevel()
            super(Window,self).__init__(self.CalendarW)
            Label(self.CalendarW, image = self.Calendar_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.CalendarW, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
            Button(self.CalendarW, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[(self.CalendarW).destroy(),self.Go_Back(self.NumberID)]).place(x=39, y=16)
            s=ttk.Style()
            s.theme_use("clam")
            self.info = Text(self.CalendarW,font = "Arial",borderwidth=0)
            self.info.place(width = 525, height = 70,x = 239, y= 530)
            Button(self.CalendarW,bd= 0 ,bg = black, activebackground=black ,image = self.ViewB, command = self.Retrieve).place(x=34, y=531)
            self.cal = Calendar(self.CalendarW,
                    font="Arial 25",
                    selectmode="day",
                    showweeknumbers = False,
                    firstweekday="monday",
                    background=black, #doesnt mean anything,
                    foreground=white, # heading writing,
                    bordercolor= black,
                    othermonthweforeground = pink,
                    othermonthwebackground = black,
                    selectbackground = blue,
                    selectforeground = pink,
                    normalbackground=black,
                    weekendbackground=black,
                    weekendforeground = blue,
                    headersbackground =black,
                    headersforeground = purple,
                    normalforeground=blue,
                    othermonthforeground = pink,
                    othermonthbackground = black,
                    date_pattern="dd/mm/yyyy")
            self.cal.place(x= 230, y =128)
        def Retrieve(self):
            self.info.delete("1.0","end")
            self.data = sqlite3.connect('NEA.A.db')
            self.SelectedDate = self.cal.get_date()
            self.cur = self.data.cursor()
            self.cur.execute('''SELECT Note
                                FROM CalendarT
                                WHERE UserID = "%s" and Date = "%s"'''%(self.NumberID,self.SelectedDate))
            try:
                self.retrieved = (self.cur.fetchone())[0] 
                self.info.insert("1.0",self.retrieved)
            except:
                pass
            self.button = Button(self.CalendarW,bd= 0 ,bg = black, activebackground=black , image =self.SaveB,command = self.Save).place(x=790,y=531)
        def Save(self):
            self.data = sqlite3.connect('NEA.A.db')
            self.SelectedDate = self.cal.get_date()
            self.cur = self.data.cursor()
            self.newinfo = self.info.get("1.0",END)
            print(self.SelectedDate)
            print(self.newinfo)
            self.temp = self.cur.execute('''SELECT* FROM CalendarT WHERE UserID = "%s" and Date = "%s"'''%(self.NumberID,self.SelectedDate));
            self.temp = self.temp.fetchone()
            self.data.commit()
            if self.temp:
                print("True")
                self.cur.execute('''UPDATE CalendarT
                                    SET Note = "%s" 
                                    WHERE UserID = "%s" and Date = "%s"'''%(self.newinfo,self.NumberID,self.SelectedDate));
                self.data.commit()
            else:
                print("False")
                self.cur.execute('''INSERT INTO CalendarT(UserID,Date,Note)
                                    VALUES ("%s", "%s","%s")'''%(self.NumberID,self.SelectedDate,self.newinfo));
                self.data.commit()
            self.data.close()
    

        def Journal_Window(self):
            nb = Notebook(self.NumberID)
            nb.Collection()
            nb.multiple()
            nb.run()
        def Condition_Window(self):
            self.CG = Toplevel()
            super(Window,self).__init__(self.CG)
            Label(self.CG, image = self.ConditionP, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.CG, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=910, y=16)
            Button(self.CG, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[(self.CG).destroy(),self.Go_Back(self.NumberID)]).place(x=39, y=15)
            def update(data):
                # Clear the listbox
                my_list.delete(0, END)

                # Add Conditions to listbox
                for item in data:
                    my_list.insert(END, item)

            # Update entry box with listbox clicked
            def fillout(e):
                # Delete whatever is in the entry box
                my_entry.delete(0, END)

                # Add clicked list item to entry box
                my_entry.insert(0, my_list.get(ANCHOR))

            # Create function to check entry vs listbox
            def check(e):
                # grab what was typed
                typed = my_entry.get()

                if typed == '':
                    data = Condition
                else:
                    data = []
                    for item in Condition:
                        if typed.lower() in item.lower():
                            data.append(item)

                # update our listbox with selected items
                update(data)				


            # Create an entry box
            my_entry = Entry(self.CG, font=("Arial", 15), width =28, bd = 0, bg= white)
            my_entry.place(x=390, y=218)
            # Create a listbox
            my_list = Listbox(self.CG, width=60, font = ("Arial", 15), bd=0, bg= purple, highlightthickness=0 ,selectbackground= blue, selectforeground= pink)
            my_list.place(x=170, y= 285)

            # Create a list of Conditions
            Condition = ["Anger", "Anxiety and panic attacks", "Bipolar disorder",
                "Body dysmorphic disorder (BDD)", "Borderline personality disorder (BPD)", "Depression", "Dissociation and dissociative disorders",
                "Eating problems", "Hearing voices", "Hoarding", "Hypomania and mania",
                "Loneliness", "Mental health problems - introduction", "Obsessive-compulsive disorder (OCD)", "Panic attacks",
                "Paranoia", "Personality disorders", "Phobias", "Postnatal depression & perinatal mental health",
                "Post-traumatic stress disorder (PTSD)", "Premenstrual dysphoric disorder (PMDD)", "Psychosis", "Recreational drugs, alcohol and addiction",
                "Schizoaffective disorder","Schizophrenia","Seasonal affective disorder (SAD)","Self-esteem",
                "Self-harm","Sleep problems","Stress","Suicidal feelings",
                "Tardive dyskinesia","Trauma"]

            # Add the Conditions to our list
            update(Condition)

            # Create a binding on the listbox onclick
            my_list.bind("<Double-Button-1>", fillout)

            # Create a binding on the entry box
            my_entry.bind("<KeyRelease>", check)
        def MyTherapist_Window(self):
            self.MT = Toplevel()
            super(Window,self).__init__(self.MT)
            Label(self.MT, image = self.MyTherapist_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.MT, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=910, y=16)
            Button(self.MT, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[(self.MT).destroy(),self.Go_Back(self.NumberID)]).place(x=39, y=15)
            Button(self.MT,image = self.AddB, command= self.Survey, bg = black,activebackground=black, bd=0).place(x=428,y=578)
            self.data = sqlite3.connect('NEA.A.db')
            self.cur = self.data.cursor()
            self.details = self.cur.execute('''SELECT DISTINCT LoginDetails.First_Name, LoginDetails.Last_Name,LoginDetails.profession, LoginDetails.UserID
                                               FROM LoginDetails,TherapistClients
                                               WHERE TherapistClients.ClientID = "%s" and TherapistClients.UserID = LoginDetails.UserID'''%(self.NumberID))
            self.detail = self.details.fetchall()
            print(self.detail)
            if len(self.detail) > 4:
                for i in range (0,4):
                    Label(self.MT,text= (self.detail[i][0]+" "+self.detail[i][1]), font = "Arial 12",fg = white,bg = black).place(x=75,y=325+(60*i))
                    Label(self.MT,text= self.detail[i][2], font = "Arial 12",fg = white,bg = black).place(x=250,y=325+(60*i))
                    Button(self.MT, image = self.RateB,bd= 0, activebackground=black, bg = black,).place(x=456,y=(309+(62*i)))
                    Button(self.MT, image = self.Chat,bd= 0, activebackground=black, bg = black,command = self.Chat_W).place(x=614,y=(309+(62*i)))
                    Button(self.MT, image = self.RemoveB,bd= 0, activebackground=black, bg = black,command =lambda:[self.Remove(self.detail[i][3])]).place(x=772,y=(309+(62*i)))
            else:
                for i in range (0,len(self.detail)):
                    Label(self.MT,text= (self.detail[i][0]+" "+self.detail[i][1]), font = "Arial 12",fg = white,bg = black).place(x=75,y=325+(60*i))
                    Label(self.MT,text= self.detail[i][2], font = "Arial 12",fg = white,bg = black).place(x=250,y=325+(60*i))
                    Button(self.MT, image = self.RateB,bd= 0, activebackground=black, bg = black,).place(x=456,y=(309+(62*i)))
                    Button(self.MT, image = self.Chat,bd= 0, activebackground=black, bg = black,command = self.Chat_W).place(x=614,y=(309+(62*i)))
                    Button(self.MT, image = self.RemoveB,bd= 0, activebackground=black, bg = black,command =lambda:[self.Remove(self.detail[i][3])]).place(x=772,y=(309+(62*i)))
        def Remove(self, TherapistID):
            print(TherapistID)
            self.data = sqlite3.connect('NEA.A.db')
            self.cur = self.data.cursor()
            self.cur.execute('''DELETE FROM TherapistClients WHERE UserID = "%s" and ClientID = "%s"'''%(TherapistID, self.NumberID))
            self.data.commit()
            self.data.close()

        def Survey(self):
            self.Survey_W = Toplevel()
            super(Window,self).__init__(self.Survey_W)
            self.Survey_W.geometry("650x900+100+100")
            Label(self.Survey_W, image = self.SurveyP, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            self.List1 = [1,2,3,4,5]
            self.List2 = ["Yes","No"]
            self.down = IntVar()
            self.anxious = IntVar()
            self.lonely = IntVar()
            self.stressed = IntVar()
            self.panic = IntVar()
            self.mood = IntVar()
            self.marriage = StringVar()
            self.family = StringVar()
            self.addiction = StringVar()
            self.trauma = StringVar()
            self.eating = StringVar()
            Button(self.Survey_W,image = self.NextB ,command = self.Therapist_Selection, bg=  black, activebackground=black,bd=0).place(x=462,y=785)
            for i in range(0,11):
                names = [self.down,self.anxious,self.lonely,self.stressed,self.panic,self.mood,self.marriage,self.family,self.addiction,self.trauma,self.eating]
                if i < 6:
                    self.Design_Position(names[i],self.List1,187.5+(35*i))
                else:
                    self.Design_Position(names[i],self.List2,60+(57*i))
        def Design_Position(self,Vname,ListN,value):
            y =OptionMenu(self.Survey_W,Vname,*ListN)
            y.place(x=467, y = value)
            y["highlightthickness"]=0
            y["borderwidth"] = 0
            y["bg"] = purple
            y["activebackground"] = purple
            y.config(width=7)
            y.config(font = "Arial 12")
        def todays_age(self,birthdate):
            today = date.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            return age
        def Therapist_Selection(self):
            self.Selection = []
            self.data = sqlite3.connect('NEA.A.db')
            self.cur = self.data.cursor()
            self.age = self.cur.execute('''SELECT DateOfBirth FROM LoginDetails WHERE UserID = "%s"'''%(self.NumberID))
            self.age = self.age.fetchone()
            if self.todays_age(datetime.datetime.strptime(self.age[0],'%d/%m/%Y')) >= 21:
                self.Name1 = ""
                self.Name2 = ""
                self.Name3 = ""
                self.Name4 = ""
                self.Name5 = ""
                self.Name6 = ""
                self.Name7 = ""
                self.Name8 = ""
                if self.anxious.get() >= 4 or self.lonely.get() >= 4:
                    self.Name3 = "social therapist"
                if self.marriage.get() == "Yes":
                    self.Name4 = "marriage and family counsellor"
                if self.family.get() == "Yes":
                    self.Name5 ="marriage and family counsellor"
                if self.addiction.get() == "Yes":
                    self.Name6 = "addiction therapist"
                if self.trauma.get() == "Yes":
                    self.name7 = "trauma therapist"
                if self.eating.get() == "Yes":
                    self.name8 = "eating disorder therapist"
                self.Name1 = "Behavioural Therapist"
                self.Name2 = "cbt therapist"
                self.Adults = self.cur.execute('''SELECT LoginDetails.First_Name,LoginDetails.Last_Name,LoginDetails.profession,
                                                            TherapistProfile.Rating,TherapistProfile.TotalClients,LoginDetails.UserID
                                                       FROM TherapistProfile, LoginDetails
                                                       WHERE (LoginDetails.profession = "%s" or LoginDetails.profession = "%s" or LoginDetails.profession = "%s" or LoginDetails.profession = "%s" or LoginDetails.profession = "%s" or LoginDetails.profession = "%s" or LoginDetails.profession = "%s" or LoginDetails.profession = "%s") and LoginDetails.UserID = TherapistProfile.UserID
                                                       ORDER BY TherapistProfile.CurrentClients,LoginDetails.profession ASC'''%(self.Name1,self.Name2,self.Name3,self.Name4,self.Name5,self.Name6,self.Name7,self.Name8))

                collection = self.Adults.fetchall()
                print(collection)
                i=0
                self.Offer(collection,i)
                
            else:
                self.Ytherapist = self.cur.execute('''SELECT LoginDetails.First_Name,LoginDetails.Last_Name,LoginDetails.profession, 
                                                              TherapistProfile.Rating,TherapistProfile.TotalClients,LoginDetails.UserID
                                                              FROM TherapistProfile, LoginDetails
                                                              WHERE LoginDetails.profession = "Youth Therapist" and LoginDetails.UserID = TherapistProfile.UserID
                                                              ORDER BY TherapistProfile.CurrentClients ASC''')
                self.data.commit()
                fetched = self.Ytherapist.fetchall()
                i=0
                self.Offer(fetched,i)
        def Offer(self, fetched,i):
            self.Offer_W = Toplevel()
            super(Window,self).__init__(self.Offer_W)
            self.Offer_W.geometry("650x900+100+100")
            percentage = int(100*fetched[i][3]/fetched[i][4])
            Label(self.Offer_W, image = self.OfferP, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.Offer_W, image = self.AcceptB, bd=0, activebackground=black, bg= black, command = lambda:[self.Accept(fetched[i][5]),self.Offer_W.destroy()]).place(x=405,y=730)
            Button(self.Offer_W, image = self.DeclineB, bd=0, activebackground=black, bg= black, command = lambda:[self.Offer_W.destroy(),self.Decline(fetched,i)]).place(x=88,y=730)
            Label(self.Offer_W,text = fetched[i][0]+" "+fetched[i][1],font = "Arial 14", fg= white, bg= black).place(x=224,y=518)
            Label(self.Offer_W,text = fetched[i][2],font = "Arial 20", fg= white, bg= black).place(x=26,y=130)
            Label(self.Offer_W,text = (fetched[i][3],"(",percentage,"%)"),font = "Arial 14", fg= white, bg= black).place(x=224,y=564)
            Label(self.Offer_W,text = fetched[i][4],font = "Arial 14", fg= white, bg= black).place(x=224,y=615)

        def Accept(self,TherapistID):
            self.cur.execute('''INSERT INTO TherapistClients (UserID,ClientID) VALUES(%s,%s)'''%(TherapistID,self.NumberID))
            self.data.commit()
        def Decline(self,fetched,i):
            if i+1 < len(fetched):
                i+=1
                self.Offer(fetched,i)
            else:
                self.Offer_W.destroy()
                self.Temp = Tk()
        def Settings_Window(self):
            self.SW = Toplevel()
            super(Window,self).__init__(self.SW)
            self.SW.geometry("650x900+100+100")

class Notebook(Window):

    def __init__(self,ID):
        self.JournalW = Toplevel()
        super(Window, self).__init__(self.JournalW)
        super(Window, self).Pictures()
        s=ttk.Style()
        s.theme_use("clam")
        self.NumberID = ID
        self.heading = StringVar()
    def Collection(self):
        Label(self.JournalW, image = self.JournalM, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
        self.notebook = ttk.Notebook(self.JournalW, width=680, height=280)
        self.data = sqlite3.connect("NEA.A.db")
        self.cur = self.data.cursor()
        self.collection = self.cur.execute('''SELECT Name, Text FROM JournalT WHERE UserID = "%s"'''%(self.NumberID))
        self.list = self.collection.fetchall()
        for i in self.list:
            self.Creation(i[0],i[1])
        tab_names = []
        for j in self.notebook.tabs():
            tab_names.append(self.notebook.tab(j, "text"))
        print(tab_names)
    def Creation(self,title,description):
        frame = ttk.Frame(self.notebook,width=680, height=280)
        Note_Entry = Text(frame)
        Note_Entry.insert("1.0", description)
        self.notebook.add(frame,text=title)
        self.notebook.place(x=156,y=227)
        Note_Entry.pack()
    def add_tab(self):
        frame = ttk.Frame(self.notebook,width=680, height=280)
        self.hello = Text(frame)
        self.hello.pack()
        self.notebook.add(frame,text=(self.heading.get()))
        self.notebook.place(x=156,y=227)
    def remove_tab(self):
        self.data = sqlite3.connect("NEA.A.db")
        self.cur = self.data.cursor()
        self.collection = self.cur.execute('''SELECT Name, Text FROM JournalT WHERE UserID = "%s"'''%(self.NumberID))
        self.list = self.collection.fetchall()
        self.Remove = self.list[self.notebook.index(self.notebook.select())]
        self.Deleting = self.cur.execute('''DELETE FROM JournalT WHERE (UserID = "%s" and Name = "%s" and Text = "%s");'''%(self.NumberID,self.Remove[0],self.Remove[1])) 
        self.data.commit()
        self.data.close()     
        self.notebook.forget(self.notebook.select()) # removes from screen
    def multiple(self):
        Button(self.JournalW, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=910, y=16)
        Button(self.JournalW, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[(self.JournalW).destroy(),self.Go_Back(self.NumberID)]).place(x=39, y=15)
        Entry(self.JournalW, textvariable=self.heading).place(x=174,y=554)
        Button(self.JournalW,image = self.Add_B, bd=0, activebackground=black, bg= black, command = self.add_tab).place(x=471,y=554)
        Button(self.JournalW,image = self.Remove_B, bd=0, activebackground=black, bg= black, command = self.remove_tab).place(x=671,y=554)
    def Go_Back(self,ID):
        back = ClientP()
        back.mainCP(ID)
    def run(self):
        self.JournalW.mainloop()
class TherapistP(Window):
        def __init__(self):
            self.TherapistP = Toplevel()
            super(Window, self).__init__(self.TherapistP)
            super(Window, self).Pictures()
            self.transfer = ClientP()
        def MainTP(self,value):
            self.NumberID = value
            Label(self.TherapistP, image = self.Therapist_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.TherapistP, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
            Button(self.TherapistP, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[self.TherapistP.destroy(),self.MainP()]).place(x=39, y=21)
            Button(self.TherapistP,width = 178, height = 84,bd=0, activebackground=black , image = self.Clients_B, bg="black", command = lambda:[self.TherapistP.destroy(), self.SymptomT_Window(self.NumberID)]).place(x= 73, y=174)
            Button(self.TherapistP,width = 178, height = 84,bd=0, activebackground=black , image = self.MyAccount_B, bg="black", command = lambda:[self.TherapistP.destroy(),self.MedicationT_Window()]).place(x= 73, y=269)
            Button(self.TherapistP,width = 178, height = 84,bd=0, activebackground=black , image = self.Calendarphoto, bg="black", command = lambda:[self.TherapistP.destroy(),self.Calendar_Window()]).place(x= 73, y=364)
            Button(self.TherapistP,width = 178, height = 84,bd=0, activebackground=black , image = self.Journal_B, bg="black", command = lambda:[self.TherapistP.destroy(),self.Journal_Window()]).place(x= 756, y=269)
            Button(self.TherapistP,width = 178, height = 84,bd=0, activebackground=black , image = self.CG_B, bg="black", command = lambda:[self.TherapistP.destroy(),self.Condition_Window()]).place(x= 756, y=174)
            Button(self.TherapistP,width = 178, height = 84,bd=0, activebackground=black , image = self.Settings_B, bg="black", command = lambda:[self.TherapistP.destroy(),self.Settings_Window()]).place(x= 756, y=364)
        def Clients(self):
            self.ClientW = Toplevel()
            super(Window,self).__init__(self.ClientW)
            Label(self.ClientW, image = self.MyTherapist_M, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
            Button(self.ClientW, image = self.Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=910, y=16)
            Button(self.ClientW, image = self.APic, bd = 0, bg = black,activebackground=black, command = lambda:[(self.ClientW).destroy(),self.Go_Back(self.NumberID)]).place(x=39, y=15)
            Button(self.ClientW,image = self.AddB, command= self.Survey, bg = black,activebackground=black, bd=0).place(x=428,y=578)
            self.data = sqlite3.connect('NEA.A.db')
            self.cur = self.data.cursor()
            self.details = self.cur.execute('''SELECT DISTINCT LoginDetails.First_Name, LoginDetails.Last_Name,LoginDetails.DateOfBirth, LoginDetails.UserID
                                               FROM LoginDetails,TherapistClients
                                               WHERE TherapistClients.ClientID = "%s" and TherapistClients.UserID = LoginDetails.UserID'''%(self.NumberID))
            self.detail = self.details.fetchall()
            print(self.detail)
            if len(self.detail) > 4:
                for i in range (0,4):
                    Label(self.ClientW,text= (self.detail[i][0]+" "+self.detail[i][1]), font = "Arial 12",fg = white,bg = black).place(x=75,y=325+(60*i))
                    Label(self.ClientW,text= self.detail[i][2], font = "Arial 12",fg = white,bg = black).place(x=250,y=325+(60*i))
                    Button(self.ClientW, image = self.RateB,bd= 0, activebackground=black, bg = black,).place(x=456,y=(309+(62*i)))
                    Button(self.ClientW, image = self.Chat,bd= 0, activebackground=black, bg = black,command = self.Chat_W).place(x=614,y=(309+(62*i)))
                    Button(self.ClientW, image = self.RemoveB,bd= 0, activebackground=black, bg = black,command =lambda:[self.Remove(self.detail[i][3])]).place(x=772,y=(309+(62*i)))
            else:
                for i in range (0,len(self.detail)):
                    Label(self.ClientW,text= (self.detail[i][0]+" "+self.detail[i][1]), font = "Arial 12",fg = white,bg = black).place(x=75,y=325+(60*i))
                    Label(self.ClientW,text= self.detail[i][2], font = "Arial 12",fg = white,bg = black).place(x=250,y=325+(60*i))
                    Button(self.ClientW, image = self.RateB,bd= 0, activebackground=black, bg = black,).place(x=456,y=(309+(62*i)))
                    Button(self.ClientW, image = self.Chat,bd= 0, activebackground=black, bg = black,command = self.Chat_W).place(x=614,y=(309+(62*i)))
                    Button(self.ClientW, image = self.RemoveB,bd= 0, activebackground=black, bg = black,command =lambda:[self.Remove(self.detail[i][3])]).place(x=772,y=(309+(62*i)))
        def Calendar_Window(self):
            self.transfer.Calendar_Window()
        def Journal_Window(self):
            self.transfer.Journal_Window()
        def Condition_Window(self):
            self.transfer.Condition_Window()
        def Settings_Window(self):
            self.transfer.Settings_Window()
        
                


Main = Window()
Main.Database() 
Main.main()

mainloop()