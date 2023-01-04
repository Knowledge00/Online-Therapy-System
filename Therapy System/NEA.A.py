from tkinter import *
import tkinter.ttk as ttk
from tkcalendar import *
import sqlite3
black = "#000000"
white = "#FFFFFF"
blue = "#32A6CC"
pink = "#CE0279"
purple = "#664193"
root = Tk()
root.withdraw()

def topB(Window,Before):
    global Arrow
    global X
    Arrow = PhotoImage(file ="Arrow.png")
    X = PhotoImage(file = "X.png")
    Back = Button(Window, image = Arrow,bg =black,bd= 0,activebackground=black, command =lambda:[Close(Window),Before])
    Back.place(x=35,y=16)
    XB = Button(Window,image = X,bd=0,bg=black, activebackground=black, command = Window.destroy ).place(x=893, y=16)
    XB.place(x=910, y=16)

def Submit(F_name,L_name,Pass,Phone,clicked,Email):
   data = sqlite3.connect('NEA.A.db')
   searcher = data.cursor()
   data.execute("INSERT INTO users VALUES (:F_name, :L_name, :Pass,:Phone, :Spec,:Email )",
                    {
                     "F_name": F_name.get(),
                     "L_name": L_name.get(),
                     "Pass": Pass.get(),
                     "Phone": Phone.get(),
                     "Spec": clicked.get(),
                     "Email": Email.get()
                    }
                )
   data.commit()
   data.close()
def Close(window):
    window.destroy()
def menu():
    Starting = Toplevel()
    Basics(Starting)
    global Scary
    global f1P
    global EmailB
    global PasswordB
    global message;
    global SignUP 
    global X
    EmailB = StringVar()
    PasswordB = StringVar()
    message = StringVar()
    SignUP = PhotoImage(file = "SignUP.png")
    f1P = PhotoImage(file = "Frame 1 (24).png")
    Scary = PhotoImage(file = "scary.png")
    X = PhotoImage(file = "X.png")
    f1p = Label(Starting,image = f1P, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    Label(Starting, text="",textvariable=message,fg=black,bg = "#473DF8",font=("Arial",12, "bold")).place(x=455,y=400)
    Entry(Starting,textvariable = EmailB,bd = 0, width = 31, font = "Arial 14").place(x=455, y=225)
    Entry(Starting,textvariable = PasswordB,bd = 0, width = 31, font = "Arial 14").place(x=455, y= 330)    
    SignInB = Button(Starting,image = Scary,activebackground=white, bd =0,command = SignIn).place(width = 92, height = 41,x=601, y=456)
    SignUPB = Button(Starting,image = SignUP,bg = black,activebackground=black, bd =0,command = lambda:[Close(Starting), User()]).place(x=74, y=402)
    XB = Button(Starting,image = X,bd=0,bg="#4E40F9", activebackground="#4E40F9", command = Starting.destroy ).place(x=908, y=16)
def Basics(Window):
    Window.resizable(0,0)
    Window.borderwidth=0
    Window.wm_attributes("-transparentcolor", "#000004")
    Window.geometry("1000x650+100+100")


def User(): 
    UW = Toplevel()
    Basics(UW)
    global TherB
    global ClientB 
    global UWB
    global X
    global Arrow
    X = PhotoImage(file = "X.png")
    UWB = PhotoImage(file = "Choice.png")
    TherB = PhotoImage(file = "TherB.png")
    ClientB = PhotoImage(file = "ClientB.png")
    Arrow = PhotoImage(file ="Arrow.png")
    pageUW = Label(UW, image = UWB, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    Therapist = Button(UW, image = TherB,bd=0, bg =black,activebackground=black,command = lambda:[Close(UW),TherSignUp()]).place(x= 95, y= 230)
    Client = Button(UW, image = ClientB,bd=0, bg =black,activebackground=black, command = lambda:[Close(UW),CustSignUp()]).place(x= 568, y =230)
    XB = Button(UW,image = X,bd=0,bg=black, activebackground=black, command = UW.destroy ).place(x=910, y=16)
    Back = Button(UW, image = Arrow,bg =black,bd= 0,activebackground=black, command =lambda:[Close(UW),menu()]).place(x=35,y=16)
def Passwork_Checker(Password,window):
     
    Special =[" ", "!", '"', "#", "$", "%", "&", "'", "(", ")", "*",
                 "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@",
                 "[", '\\', "]", "^", "_", "`", "{", "|", "}", "~"]
    val = True
    short = Label(window,text= 'length should be at least 6')
    if len(Password) < 6:
        short.grid()
        val = False
          
    if len(Password) > 12:
        Label(window,text= 'length should be not be greater than 8')
        val = False
          
    if not any(char.isdigit() for char in Password):
        Label(window,text= 'Password should have at least one number')
        val = False
          
    if not any(char.isupper() for char in Password):
        Label(window,text= 'Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in Password):
        Label(window,text= 'Password should have at least one lowercase letter')
        val = False
          
    if not any(char in Special for char in Password):
        Label(window,text= 'Password should have at least one of the special symbol')
        val = False
    else:
        return val
def DataBase():
    data = sqlite3.connect('NEA.A.db')
    searcher = data.cursor()
    data.execute('''CREATE TABLE IF NOT EXISTS users (
                "First_Name" text,
                "Last_Name" text,
                "Password" TEXT,
                "Phone_Number" text,
                "profession" text,
                "Email" text
                )''')
                
    data.commit()
    data.close()
def CustSignUp():
    CSUW = Toplevel()
    Basics(CSUW)
    global RegClient
    global CA
    global X
    global Arrow
    CA = PhotoImage(file = "CA.png")
    X= PhotoImage(file = "X.png")
    Arrow = PhotoImage(file = "Arrow.png")
    RegClient = PhotoImage(file = "RegClient.png")
    BackgroundRegC = Label(CSUW, image = RegClient, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    XB = Button(CSUW,image = X,bd=0,bg=black, activebackground=black, command = CSUW.destroy ).place(x=910, y=16)
    Back = Button(CSUW, image = Arrow,bg =black,bd= 0,activebackground=black, command =lambda:[Close(CSUW),User()]).place(x=35,y=16)
    F_name = Entry(CSUW,width = 21,bd =0, font = "Arial 15")
    F_name.place(x=122,y=230)
    L_name = Entry(CSUW,width = 21,bd =0, font = "Arial 15")
    L_name.place(x=539,y=230)
    Email = Entry(CSUW,width = 21,bd =0, font = "Arial 15")
    Email.place(x=122,y=328)
    Phone = Entry(CSUW,width = 21,bd =0, font = "Arial 15")
    Phone.place(x=539,y=328)
    Pass = Entry(CSUW,width = 21,bd =0, font = "Arial 15")
    Pass.place(x=122,y=419)
    CPass = Entry(CSUW,width = 21,bd =0, font = "Arial 15")
    CPass.place(x=539, y=419)
    clicked = StringVar(CSUW)
    clicked.set(" ")
    Job = ["marriage and family counselor", "addiction therapist", "behavioural therapist",
           "cognitive/cbt therapist", "eating disorder therapist",
            "youth therapist (ages 10-21)",
           "trauma therapist", "social therapist"]
    Prof = OptionMenu(CSUW,clicked ,*Job)
    Check = Button(CSUW, image = CA, bd = 0, bg = black,activebackground=black, command = lambda:[menu(),Submit(F_name,L_name,Pass,Phone,clicked,Email), Close(CSUW)]).place(x= 113,y=519)
def TherSignUp():
    TSUW = Toplevel()
    Basics(TSUW)
    global RegTheraR
    global CA
    global X
    global Arrow
    Arrow = PhotoImage(file ="Arrow.png")
    X = PhotoImage(file = "X.png")
    CA = PhotoImage(file = "CA.png")
    RegTheraR = PhotoImage(file = "TheraR.png")
    BackgroundRegC = Label(TSUW, image = RegTheraR, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    XB = Button(TSUW,image = X,bd=0,bg=black, activebackground=black, command = TSUW.destroy ).place(x=910, y=16)
    F_name = Entry(TSUW,width = 21,bd =0, font = "Arial 15")
    F_name.place(x=70,y=195)
    L_name = Entry(TSUW,width = 21,bd =0, font = "Arial 15")
    L_name.place(x=378, y=195)
    Email = Entry(TSUW,width = 21,bd =0, font = "Arial 15")
    Email.place(x=676, y=195)
    Phone = Entry(TSUW,width = 21,bd =0, font = "Arial 15")
    Phone.place(x=70, y=305)
    Pass = Entry(TSUW,width = 21,bd =0, font = "Arial 15")
    Pass.place(x=378,y=305)
    CPass = Entry(TSUW,width = 21,bd =0, font = "Arial 15")
    CPass.place(x=676,y=305)
    clicked = StringVar(TSUW)
    clicked.set("Field of work")
    Job = ["marriage and family counselor", "addiction therapist", "behavioural therapist",
           "cognitive/cbt therapist", "eating disorder therapist",
            "youth therapist (ages 10-21)",
           "trauma therapist", "social therapist"]
    Prof = OptionMenu(TSUW,clicked ,*Job)
    s=ttk.Style()
    s.theme_use("clam")
    Prof["highlightthickness"]=0
    Prof["borderwidth"] = 0
    Prof["bg"] = white
    Prof["activebackground"] = white
    Prof.config(width=23)
    Prof.config(font = "Arial 12")
    Prof.place(x=378,y=412)
    Back = Button(TSUW, image = Arrow,bg =black,bd= 0,activebackground=black, command =lambda:[Close(TSUW), User()])
    Back.place(x=35,y=16)
    Next = Button(TSUW, image = CA,bg =black,bd= 0,activebackground=black,command =lambda:[Submit(F_name,L_name,Pass,Phone,clicked,Email),Close(TSUW),menu()])
    Next.place(x=115, y= 480)
def SignInP():
    SIP = Toplevel()
    Basics(SIP)
    global EmailB
    global PasswordB
    global message;
    EmailB = StringVar()
    PasswordB = StringVar()
    message = StringVar()
    Label(SIP, text="",textvariable=message,bg="#1C2833",fg="white",font=("Arial",12,"bold")).place(x=95,y=120)
    Entry(SIP,textvariable = EmailB, width = 45).place(x=100, y=60)
    Entry(SIP,textvariable = PasswordB, width = 45).place(x=100, y= 80)    
    Lock = Button(SIP, text = "Sign-In",command = SignIn).place(x=250, y=200)
    
def SignIn():
    Email = EmailB.get()
    Password = PasswordB.get()
    Useless = " "
    if Email == "" or Password == "":
         message.set("One or Both Entries have been left Empty!")
    else:
        data = sqlite3.connect("NEA.A.db")
        cursor = data.execute('SELECT * from users where Email="%s" and Password="%s"'%(Email,Password));
        if cursor.fetchone():
            additional = data.execute('SELECT * from users where Email="%s" and Password="%s" and profession= "%s"'%(Email,Password, Useless));
            if additional.fetchone():
                MainP()
            else:
                TherMP()
        else:
            message.set("Wrong username or password!!!")
def SymptomT_Window():
    STW = Toplevel()
    Basics(STW)
    global Xpic
    global APic
    global STPic
    STPic = PhotoImage(file = "Frame 1 (14).png")
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    MPicS = Label(STW, image = STPic, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    XB1 = Button(STW, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB2 = Button(STW, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(STW),MainP()]).place(x=39, y=21)
def MedicationT_Window():
    MTW = Toplevel()
    Basics(MTW)
    global Xpic
    global APic
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    XB = Button(MTW, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB = Button(MTW, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(MTW),MainP()]).place(x=39, y=21)
def Calendar_Window():
    CAW = Toplevel()
    Basics(CAW)
    global Xpic
    global APic
    global Cmain
    global EditP
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    Cmain = PhotoImage(file = "Calendar.png")
    EditP = PhotoImage(file = "Group 2 (4).png")
    CAPic = Label(CAW, image = Cmain, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    XB = Button(CAW, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB = Button(CAW, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(CAW),MainP()]).place(x=39, y=21)
    s=ttk.Style()
    s.theme_use("clam")
    SCal = Text(CAW,font = "Arial",borderwidth=0).place(width = 525, height = 70,x = 239, y= 530)
    EditB = Button(CAW, text= "hello",bd= 0 ,bg = black, activebackground=black ,image = EditP).place(x=34, y=531)
    cal = Calendar(CAW,
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
               date_pattern="dd-mm-yyyy")
    cal.place(x= 230, y =128)
    def grad_date(): 
        date.config(cal.get_date()) 
    Button(root, text = "Get Date", 
        command = grad_date).pack(pady = 20) 
    date = Label(root, text = "") 
    date.pack(pady = 20) 
def Journal_Window():
    JOW = Toplevel()
    Basics(JOW)
    global Xpic
    global APic
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    XB = Button(JOW, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB = Button(JOW, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(JOW),MainP()]).place(x=39, y=21)
def Condiiton_Window():
    COG = Toplevel()
    Basics(COG)
    global COGB
    global FindB
    global Xpic
    global APic
    FindB = PhotoImage(file ="Find.png")
    COGB = PhotoImage(file = "COGB.png")
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    COGBL = Label(COG, image = COGB, bg = "#000004").place(x=0,y=0, relwidth = 1, relheight = 1)
    XB = Button(COG, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB = Button(COG, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(COG),MainP()]).place(x=39, y=21)
    SearchBar = Entry(COG, width  = 36, font = "Arial 13", bd = 0).place(x = 383, y = 222)
    Find = Button(COG, width = 72, height = 35, image = FindB, activebackground=black,bd=0, bg = black ).place(x=740, y= 214)
    Info = Entry(COG, state = "disabled", border =0, disabledbackground = white).place(width = 730, height = 344, x = 135, y = 270)
def Settings_Window():
    SEW = Toplevel()
    Basics(SEW)
    global Xpic
    global APic
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    XB = Button(SEW, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB = Button(SEW, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(SEW),MainP()]).place(x=39, y=21)
def MainP():
    Main = Toplevel()
    Basics(Main)
    global Xpic
    global APic
    global b1g
    global SymptomTphoto
    global MedicationTphoto
    global Calendarphoto
    global Chatphoto
    global Journalphoto
    global CaGphoto
    global Settingsphoto
    b1g = PhotoImage(file = "Frame 1 (13).png")
    Xpic = PhotoImage(file = "X.png")
    APic = PhotoImage(file = "Arrow.png")
    SymptomTphoto = PhotoImage(file ="Group 3 (1).png")
    MedicationTphoto = PhotoImage(file ="Group 2 (2).png")
    Calendarphoto = PhotoImage(file ="Group 2 (3).png")
    #Chatphoto = PhotoImage(file ="Group 4 (1).png")#
    Journalphoto = PhotoImage(file ="Group 5 (1).png")
    CaGphoto = PhotoImage(file ="Group 6 (1).png")
    Settingsphoto = PhotoImage(file ="Group 8.png")
    my_label = Label(Main, image = b1g, bg = "#000004")
    my_label.place(x=0,y=0, relwidth = 1, relheight = 1)
    XB = Button(Main, image = Xpic, bd = 0, bg = black,activebackground=black, command = root.destroy).place(x=893, y=16)
    AB = Button(Main, image = APic, bd = 0, bg = black,activebackground=black, command = lambda:[Close(Main),MainP()]).place(x=39, y=21)
    SymptomTB = Button(Main,width = 178, height = 84,bd=0, activebackground=black , image = SymptomTphoto, bg="black", command = lambda:[Close(Main), SymptomT_Window()])
    SymptomTB.place(x= 73, y=174)
    MedicationTB = Button(Main,width = 178, height = 84,bd=0, activebackground=black , image = MedicationTphoto, bg="black", command = lambda:[Close(Main),MedicationT_Window()])
    MedicationTB.place(x= 73, y=269)
    CalendarB = Button(Main,width = 178, height = 84,bd=0, activebackground=black , image = Calendarphoto, bg="black", command = lambda:[Close(Main),Calendar_Window()])
    CalendarB.place(x= 73, y=364)
    #ChatB = Button(Main,width = 120, height = 100,bd=0, image = Chatphoto, bg="#707173")#
    #ChatB.place(x= 392, y=505)#
    JournalB =Button(Main,width = 178, height = 84,bd=0, activebackground=black , image = Journalphoto, bg="black", command = lambda:[Close(Main),Journal_Window()])
    JournalB.place(x= 756, y=269)
    CoGB = Button(Main,width = 178, height = 84,bd=0, activebackground=black , image = CaGphoto, bg="black", command = lambda:[Close(Main),Condiiton_Window()])
    CoGB.place(x= 756, y=174)
    SettingsB = Button(Main,width = 178, height = 84,bd=0, activebackground=black , image = Settingsphoto, bg="black", command = lambda:[Close(Main),Settings_Window()])
    SettingsB.place(x= 756, y=364)
def TherMP():
    TMP = Toplevel()
    Basics(TMP)
Calendar_Window()
DataBase()
mainloop()
Calendar_Window()
