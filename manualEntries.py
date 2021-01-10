import tkinter 
from tkinter import *



#  variables for tkinter properties
labelfont = 'helvetica 12 italic'
labelFG = 'gray26'
labelBG  = 'white'
inputfont = 'helvetica 14'
inputFG = 'black'
inputBG = 'gray91'
inputBG2 = 'gray70'
paddingX =3 
paddingY =5


# this list is utilized by manual walk entry function
entryMainWalk = []
titlerW =['name','res no','hotel','company','group','travel agent']


# asks users if they need to enter a walk no show or late cxl manually

def manuaQ(arrivalsMainVar,walkDataVar,LateCxlDataVar):
    windowMain = Tk()
    # creates title in windowMain border
    windowMain.title('OPERA Night Audit Manager Pack creator')
    windowMain.configure(background ='white')
    windowMain.geometry('200x500')




# function to manually enter walked reservations
    def manualWalkEntry(walkDataVar):
        def entryMainWalkPrinter():
            output.delete(0.0,END)
            for x in range (len(entryMainWalk)):
                output.insert(END,f'\n       ENTRY: {x}__________')
                for y in range(len(entryMainWalk[x])):
                    output.insert(END,f'  {titlerW[y]} / {entryMainWalk[x][y]}     ')
        
        def clickWalk():
            entryWalkAdder =[]
        #     this collects whatever is typed into input window
            entered_text = inputbox1.get()
            entryWalkAdder.append(entered_text)
            
            entered_text2 = inputbox2.get()
            entryWalkAdder.append(entered_text2)
            
            entered_text3 = inputbox3.get()
            entryWalkAdder.append(entered_text3)
            
            entered_text4 = inputbox4.get()
            entryWalkAdder.append(entered_text4)
            
            entered_text5 = inputbox5.get()
            entryWalkAdder.append(entered_text5)
            
            entered_text6 = inputbox6.get()
            entryWalkAdder.append(entered_text6)
            
            entryMainWalk.append(entryWalkAdder)
            print(entryMainWalk)
            entryMainWalkPrinter()
            inputbox1.delete(0,END)
            inputbox2.delete(0,END)
            inputbox3.delete(0,END)
            inputbox4.delete(0,END) 
            inputbox5.delete(0,END)
            inputbox6.delete(0,END)
            
            


        windowWalk = Toplevel(windowMain)
        # creates title in windowWalk border
        windowWalk.title('OPERA Night Audit Manager Pack creator')
        windowWalk.configure(background ='white')
        windowWalk.geometry('1920x400')
        # sets properties of the windowWalk


    #     # # sets properties of an image in the windowWalk and creates it
    #     photo1 = PhotoImage(file = 'oprah.gif', format = 'gif -index 2')
    #     Label (windowWalk, image = photo1, bg= 'gray') .grid(row =0, column = 2, sticky =E)


        # sets properties and creates text in the windowWalk ... bg is text background fg is(foreground) color for font
        Label (windowWalk, text='Manually Enter - Walked Guests',bg = labelBG, fg='black', font='helvetica 15 italic') .grid (row = 0,column='0', sticky = E)
        Label (windowWalk, text='Walked',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='0', sticky = E)
        Label (windowWalk, text='Res No.',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='1', sticky = E)
        Label (windowWalk, text='Hotel',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='2', sticky = E)
        Label (windowWalk, text='Company',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='3', sticky = E)
        Label (windowWalk, text='Group',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='4', sticky = E)
        Label (windowWalk, text='Travel Agent',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='5', sticky = E)



        # sets properties and creates input windowWalk
        inputbox1 = Entry(windowWalk, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox1.grid(row = 3, column = 0,padx = paddingX, pady= paddingY, sticky = E)
        inputbox2 = Entry(windowWalk, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox2 .grid(row = 3, column = 1,padx = paddingX, pady= paddingY, sticky = E)
        inputbox3 = Entry(windowWalk, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox3 .grid(row = 3, column = 2,padx = paddingX, pady= paddingY, sticky = E)
        inputbox4 = Entry(windowWalk, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox4 .grid(row = 3, column = 3,padx = paddingX, pady= paddingY, sticky = E)
        inputbox5 = Entry(windowWalk, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox5 .grid(row = 3, column = 4,padx = paddingX, pady= paddingY, sticky = E)
        inputbox6 = Entry(windowWalk, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox6 .grid(row = 3, column = 5,padx = paddingX, pady= paddingY, sticky = E)
        
        def walkmanEnd():
            print('clicked~~~')
            for et in range(len(entryMainWalk)):
                walkDataVar.append(entryMainWalk[et])
            windowWalk.destroy()

        removeChoice = ['x']

        def clickRemove():
            print('pass')
            entryMainWalk.pop(int(removeChoice[0]))
            entryMainWalkPrinter()
        def clickPop():
            removerEnt = removerQ.get()
            removerQ.delete(0,END)
            print(removerEnt)
            removeChoice[0]= removerEnt
            clickRemove()
            
        output = Text(windowWalk, width = 150, height= 10, wrap= WORD, background = labelBG, fg = 'blue', border=0,font = labelfont)
        output.grid (row = 5,column='0',columnspan= 6, sticky = W)
        

        removerQ = Entry(windowWalk, width = 4, bg='gray90' ,fg='red' ,font = inputfont,justif='center')
        removerQ .grid(row = 9, column =5,padx = 80, pady= paddingY, sticky =E )
        btn3=Button(windowWalk, text='Remove',background = 'red',fg ='white',width = 9, command = clickPop) .grid(row= 9, column= 5, sticky = E)
        
        # set properties and creates submit button

        btn1=Button(windowWalk, text='Submit',width = 6,background = 'gray36',fg='white',command = clickWalk) .grid(row= 3, column= 6, sticky = E)
        
        btn2=Button(windowWalk, text='Done',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue', command = walkmanEnd) .grid(row= 9, padx=25, column= 0, sticky = W)

        windowWalk.mainloop()

        print(walkDataVar)



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



    # this list is utilized by manual late cxl entry function
    entryMainLCxl = []
    titlerLC =['name','res no','reason','company','group','travel agent']


    # function to manually enter walked reservations
    def manualLCXLEntry(LateCxlDataVar):
        def entryMainLCxlPrinter():
            output.delete(0.0,END)
            for x in range (len(entryMainLCxl)):
                output.insert(END,f'\n       ENTRY: {x}__________')
                for y in range(len(entryMainLCxl[x])):
                    output.insert(END,f'  {titlerLC[y]} / {entryMainLCxl[x][y]}     ')
        
        def clickWalk():
            entryLCxlAdder =[]
        #     this collects whatever is typed into input window
            entered_text = inputbox1.get()
            entryLCxlAdder.append(entered_text)
            
            entered_text2 = inputbox2.get()
            entryLCxlAdder.append(entered_text2)
            
            entered_text3 = inputbox3.get()
            entryLCxlAdder.append(entered_text3)
            
            entered_text4 = inputbox4.get()
            entryLCxlAdder.append(entered_text4)
            
            entered_text5 = inputbox5.get()
            entryLCxlAdder.append(entered_text5)
            
            entered_text6 = inputbox6.get()
            entryLCxlAdder.append(entered_text6)
            
            entryMainLCxl.append(entryLCxlAdder)
            print(entryMainLCxl)
            entryMainLCxlPrinter()
            inputbox1.delete(0,END)
            inputbox2.delete(0,END)
            inputbox3.delete(0,END)
            inputbox4.delete(0,END) 
            inputbox5.delete(0,END)
            inputbox6.delete(0,END)
            
            


        windowCXL = Toplevel(windowMain)
        # creates title in window border
        windowCXL.title('OPERA Night Audit Manager Pack creator')
        windowCXL.configure(background ='white')
        windowCXL.geometry('1920x400')
        # sets properties of the windowCXL


    #     # # sets properties of an image in the windowCXL and creates it
    #     photo1 = PhotoImage(file = 'oprah.gif', format = 'gif -index 2')
    #     Label (windowCXL, image = photo1, bg= 'gray') .grid(row =0, column = 2, sticky =E)


        # sets properties and creates text in the windowCXL ... bg is text background fg is(foreground) color for font
        Label (windowCXL, text='Manually Enter - Late Cxl reservations',bg = labelBG, fg='black', font='helvetica 15 italic') .grid (row = 0,column='0', sticky = E)
        Label (windowCXL, text='Late Cxl',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='0', sticky = E)
        Label (windowCXL, text='Res No.',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='1', sticky = E)
        Label (windowCXL, text='Reason',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='2', sticky = E)
        Label (windowCXL, text='Company',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='3', sticky = E)
        Label (windowCXL, text='Group',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='4', sticky = E)
        Label (windowCXL, text='Travel Agent',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='5', sticky = E)



        # sets properties and creates input windowCXL
        inputbox1 = Entry(windowCXL, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox1.grid(row = 3, column = 0,padx = paddingX, pady= paddingY, sticky = E)
        inputbox2 = Entry(windowCXL, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox2 .grid(row = 3, column = 1,padx = paddingX, pady= paddingY, sticky = E)
        inputbox3 = Entry(windowCXL, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox3 .grid(row = 3, column = 2,padx = paddingX, pady= paddingY, sticky = E)
        inputbox4 = Entry(windowCXL, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox4 .grid(row = 3, column = 3,padx = paddingX, pady= paddingY, sticky = E)
        inputbox5 = Entry(windowCXL, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox5 .grid(row = 3, column = 4,padx = paddingX, pady= paddingY, sticky = E)
        inputbox6 = Entry(windowCXL, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox6 .grid(row = 3, column = 5,padx = paddingX, pady= paddingY, sticky = E)
        
        def CxlmanEnd():
            print('clicked~~~')
            for et in range(len(entryMainLCxl)):
                LateCxlDataVar.append(entryMainLCxl[et])
            windowCXL.destroy()

        removeChoice = ['x']

        def clickRemove():
            print('pass')
            entryMainLCxl.pop(int(removeChoice[0]))
            entryMainLCxlPrinter()
        def clickPop():
            removerEnt = removerQ.get()
            removerQ.delete(0,END)
            print(removerEnt)
            removeChoice[0]= removerEnt
            clickRemove()
            
        output = Text(windowCXL, width = 150, height= 10, wrap= WORD, background = labelBG, fg = 'blue', border=0,font = labelfont)
        output.grid (row = 5,column='0',columnspan= 6, sticky = W)
        

        removerQ = Entry(windowCXL, width = 4, bg='gray90' ,fg='red' ,font = inputfont,justif='center')
        removerQ .grid(row = 9, column =5,padx = 80, pady= paddingY, sticky =E )
        btn3=Button(windowCXL, text='Remove',background = 'red',fg ='white',width = 9, command = clickPop) .grid(row= 9, column= 5, sticky = E)
        
        # set properties and creates submit button

        btn1=Button(windowCXL, text='Submit',width = 6,background = 'gray36',fg='white',command = clickWalk) .grid(row= 3, column= 6, sticky = E)
        
        btn2=Button(windowCXL, text='Done',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue', command = CxlmanEnd) .grid(row= 9, padx=25, column= 0, sticky = W)

        windowCXL.mainloop()

        print(LateCxlDataVar)







    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>








    # this list is utilized by manual no show entry function
    entryMain = []
    titler =['name','res no','nights','company','group','travel agent']
    # function called by submit button




    # allows user to manually enter noshows that are not in the arrival list

    def manualNOshowEntry(arrivalsMainVar):
        def entryMainPrinter():
            output.delete(0.0,END)
            for x in range (len(entryMain)):
                output.insert(END,f'\n       ENTRY: {x}__________')
                for y in range(len(entryMain[x])):
                    output.insert(END,f'  {titler[y]} / {entryMain[x][y]}     ')
        
        def click():
            entryAdder =[]
        #     this collects whatever is typed into input window
            entered_text = inputbox1.get()
            entryAdder.append(entered_text)
            
            entered_text2 = inputbox2.get()
            entryAdder.append(entered_text2)
            
            entered_text3 = inputbox3.get()
            entryAdder.append(entered_text3)
            
            entered_text4 = inputbox4.get()
            entryAdder.append(entered_text4)
            
            entered_text5 = inputbox5.get()
            entryAdder.append(entered_text5)
            
            entered_text6 = inputbox6.get()
            entryAdder.append(entered_text6)
            
            entryMain.append(entryAdder)
            print(entryMain)
            entryMainPrinter()
            inputbox1.delete(0,END)
            inputbox2.delete(0,END)
            inputbox3.delete(0,END)
            inputbox4.delete(0,END) 
            inputbox5.delete(0,END)
            inputbox6.delete(0,END)
            
            


        window = Toplevel(windowMain)
        # creates title in window border
        window.title('OPERA Night Audit Manager Pack creator')
        window.configure(background ='white')
        window.geometry('1920x400')
        # sets properties of the window


    #     # # sets properties of an image in the window and creates it
    #     photo1 = PhotoImage(file = 'oprah.gif', format = 'gif -index 2')
    #     Label (window, image = photo1, bg= 'gray') .grid(row =0, column = 2, sticky =E)

        labelfont = 'helvetica 12 italic'
        labelFG = 'gray26'
        labelBG  = 'white'
        # sets properties and creates text in the window ... bg is text background fg is(foreground) color for font
        Label (window, text='Manually Enter - No shows',bg = labelBG, fg='black', font='helvetica 15 italic') .grid (row = 0,column='0', sticky = E)
        Label (window, text='No show',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='0', sticky = E)
        Label (window, text='Res No.',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='1', sticky = E)
        Label (window, text='Nights',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='2', sticky = E)
        Label (window, text='Company',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='3', sticky = E)
        Label (window, text='Group',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='4', sticky = E)
        Label (window, text='Travel Agent',bg = labelBG, fg=labelFG, font=labelfont) .grid (row = 1,column='5', sticky = E)



        # sets properties and creates input window
        inputbox1 = Entry(window, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox1.grid(row = 3, column = 0,padx = paddingX, pady= paddingY, sticky = E)
        inputbox2 = Entry(window, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox2 .grid(row = 3, column = 1,padx = paddingX, pady= paddingY, sticky = E)
        inputbox3 = Entry(window, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox3 .grid(row = 3, column = 2,padx = paddingX, pady= paddingY, sticky = E)
        inputbox4 = Entry(window, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox4 .grid(row = 3, column = 3,padx = paddingX, pady= paddingY, sticky = E)
        inputbox5 = Entry(window, width = 20, bg=inputBG,fg=inputFG ,font = inputfont)
        inputbox5 .grid(row = 3, column = 4,padx = paddingX, pady= paddingY, sticky = E)
        inputbox6 = Entry(window, width = 20, bg=inputBG2 ,fg=inputFG ,font = inputfont)
        inputbox6 .grid(row = 3, column = 5,padx = paddingX, pady= paddingY, sticky = E)
        
        def closer():
            print('clicked~~~')
            for et in range(len(entryMain)):
                arrivalsMainVar.append(entryMain[et])
            window.destroy()

        removeChoice = ['x']

        def clickRemove():
            print('pass')
            entryMain.pop(int(removeChoice[0]))
            entryMainPrinter()


        def clickPop():
            removerEnt = removerQ.get()
            removerQ.delete(0,END)
            print(removerEnt)
            removeChoice[0]= removerEnt
            clickRemove()
            
        output = Text(window, width = 150, height= 10, wrap= WORD, background = labelBG, fg = 'blue', border=0,font = labelfont)
        output.grid (row = 5,column='0',columnspan= 6, sticky = W)
        

        removerQ = Entry(window, width = 4, bg='gray90' ,fg='red' ,font = inputfont,justif='center')
        removerQ .grid(row = 9, column =5,padx = 80, pady= paddingY, sticky =E )
        btn3=Button(window, text='Remove',background = 'red',fg ='white',width = 9, command = clickPop) .grid(row= 9, column= 5, sticky = E)
        
        # set properties and creates submit button

        btn1=Button(window, text='Submit',width = 6,background = 'gray36',fg='white',command = click) .grid(row= 3, column= 6, sticky = E)
        
        btn2=Button(window, text='Done',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue', command = closer) .grid(row= 9, padx=25, column= 0, sticky = W)


        window.mainloop()
        print(arrivalsMainVar)



    def manWalk():
        manualWalkEntry(walkDataVar)
        
    def manNoS():
        manualNOshowEntry(arrivalsMainVar)
        
    def manCxl():
        manualLCXLEntry(LateCxlDataVar)

    def no():
        print('no')
        lbl2['text']= f'ok cool'
        windowMain.after(500,windowMain.destroy)
            
    
    lbl1 = Label (windowMain, text='Do you need\nto manually enter\n any of the ff:?',bg = labelBG, fg='black', font='helvetica 15 italic')
    lbl1.grid (row = 0,column='0',padx = 5,pady=10, sticky = N)
       
    lbl2 = Label (windowMain, text='',bg = labelBG, fg='red', font=labelfont)
    lbl2.grid (row = 2,column='0',padx = 5,pady=0, sticky = N)
    
    Button(windowMain, text='No Show',font='helvetica 10 italic',width = 9,height=4,background ='dodger blue',  command =manNoS ) .grid(row= 2, column= 0,padx=25, pady =10, sticky = N)
    Button(windowMain, text='Walk',font='helvetica 10 italic',width = 9,height=4,background ='deep sky blue',  command = manWalk) .grid(row= 3, column= 0,padx=25, pady =10, sticky = N)
    Button(windowMain, text='Late Cxl',font='helvetica 10 italic',width = 9,height=4,background ='blue2',  command = manCxl) .grid(row= 4, column= 0,padx=25, pady =10, sticky = N)

    Button(windowMain, text='NoNe',fg='white',font='helvetica 10 italic',width = 9,height=4,background ='red' ,command = no) .grid(row= 5, column= 0,padx=25,pady =10, sticky = N)

    
#     punch = Button(windowMain, text='Submit',width = 6, command = response) 
#     punch.grid(row= 2, column= 0, sticky = N)


    windowMain.mainloop()



























