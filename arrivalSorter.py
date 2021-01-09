import tkinter 
from tkinter import *
from threading import Timer

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


# this function asks user if  any of the arrivals are no show / late cxl / walks
from threading import Timer

Arrived= [['Name', 'ResNo.', 'Nights', 'Company', 'Group', 'Travel Agent']]
# this function asks user if  any of the arrivals are no show / late cxl / walks
def arrivalOPTs(Inbound,walkDataVar,LateCXlDataVar):
    walksChoice = ['y']
    walksHotel = ['y1']
    
    lateCXLchoice = ['x']
    lateCXLreason = ['x1']

    arrivedChoice = ['z']
    
    arrivals = []

    window = Tk()
    # creates title in window border
    window.title('OPERA Night Audit Manager Pack creator')
    window.configure(background ='white')
    window.geometry('1920x400')
        

    def entryMainPrinter():
        output.delete(0.0,END)
        for x in range (1,len(arrivals)):
            output.insert(END,f'\nENTRY: {x}')
            for y in range(len(arrivals[x])):
                output.insert(END,f'  {Inbound[0][y]} / {arrivals[x][y]}     ')
    
    def entryWalkPrinter():
        output.delete(0.0,END)
        for x in range (1,len(walkDataVar)):
            output.insert(END,f'\nWALKED: {x}')
            for y in range(len(walkDataVar[x])):
                output.insert(END,f'  {walkDataVar[0][y]} / {walkDataVar[x][y]}     ')
    
    def entryLateCxlPrinter():
        output.delete(0.0,END)
        for x in range (1,len(LateCXlDataVar)):
            output.insert(END,f'\nLate CXL: {x}')
            for y in range(len(LateCXlDataVar[x])):
                output.insert(END,f'  {LateCXlDataVar[0][y]} / {LateCXlDataVar[x][y]}     ')
    
    def entryArrPrinter():
        output.delete(0.0,END)
        for x in range (1,len(Arrived)):
            output.insert(END,f'\nARRIVED: {x}')
            for y in range(len(Arrived[x])):
                output.insert(END,f'  {Arrived[0][y]} / {Arrived[x][y]}     ')        

    def walkEntry():
        print('walker')
        walkE = int(inputboxWalk.get())
        inputboxWalk.delete(0,END)
        walksChoice[0] = walkE
        print(walksChoice[0])
        walkDataVar.append(arrivals[walkE])
        print(walkDataVar)

        print(f'jboooXXXXXXXXXXXXXXXXXXXXXXXxoooooo{arrivals}')
        Inbound.clear()
        print(Inbound)
        for x in range (len(arrivals)):
            Inbound.append(arrivals[x])
        arrivals.pop(walkE)
        print(Inbound)



        print(walkDataVar)
        print(f'jboooooooooooooooooooooooooooo{arrivals}')
        print(Inbound)

        walkTo = inputboxWalkRs.get()
        inputboxWalkRs.delete(0,END)
        walkDataVar[-1][2] = walkTo

        print(walkDataVar)


        entryWalkPrinter()
        w = Timer(2, entryMainPrinter)
        w.start()
        
    def walkView():
        entryWalkPrinter()
        w = Timer(5, entryMainPrinter)
        w.start()

    def lateView():
        entryLateCxlPrinter()
        l = Timer(5, entryMainPrinter)
        l.start()
        
    def arrView():
        entryArrPrinter()
        a = Timer(5, entryMainPrinter)
        a.start()
        
        
    def lateCxlEntry():
        print('cxl')
        lateE = int(inputboxLateCxl.get())
        inputboxLateCxl.delete(0,END)
        lateCXLchoice[0] = lateE
        print(lateCXLchoice[0])
        lateRsn = inputboxLateCxlRs.get()
        inputboxLateCxlRs.delete(0,END)
        arrivals[lateE][2] = lateRsn
        LateCXlDataVar.append(arrivals[lateE])
        arrivals.pop(lateE)
        print(LateCXlDataVar)
        print(arrivals)
        entryLateCxlPrinter()
        l = Timer(2, entryMainPrinter)
        l.start()
        
    
    
    def ArrivedEntry():
        print('arred')
        arrPop = int(inputboxArrvd.get())
        inputboxArrvd.delete(0,END)
        Arrived.append(arrivals[arrPop])
        arrivals.pop(arrPop)
        entryArrPrinter()
        a = Timer(2, entryMainPrinter)
        a.start()        

        
    def fin():
        print('clicked~~~finito')
        Inbound.clear()
        for bb in range(len(arrivals)):
            Inbound.append(arrivals[bb])
        print(Inbound)
        window.destroy()
        
#     header        
    Label (window, text='Are any of these arrivals WALKS or LATE CXL?',bg = labelBG, fg=labelFG, font=labelfont) .grid (row =0,column=0,padx =25,pady =20, sticky = W) 
    output = Text(window, width = 200, height= 4, wrap= WORD, background = labelBG, fg = 'blue', border=0,font = labelfont)
    output.grid (row = 1,column=0,columnspan=2, padx = 25,pady=0, sticky = W)    

    
#     Walk input and labels
    Label(window, text= 'Walked Reservation',bg = labelBG, fg=labelFG, font=labelfont) .grid (row=5,column=0,padx = 25,sticky = W) 
    inputboxWalk = Entry(window, width = 4, bg=inputBG,fg=inputFG ,font = inputfont)
    inputboxWalk.grid(row = 5, column = 0,padx = 185, pady= 0, sticky = W)
    
    Label(window, text= 'Hotel',bg = labelBG, fg=labelFG, font=labelfont) .grid (row=5,column=0, padx = 275,sticky = W) 
    inputboxWalkRs = Entry(window, width = 15, bg=inputBG,fg=inputFG ,font = inputfont)
    inputboxWalkRs.grid(row = 5, column = 0,padx =330, pady=10, sticky = W)
    
#     button for walk submit
    walkBUTT=Button(window, text='Walk',width = 6, background = 'gray36',fg='white',command = walkEntry) .grid(row=5, column= 0,padx =515, pady= 10,sticky = W)
    walkView =Button(window, text='View',width = 6, command = walkView) .grid(row=5, column= 0,padx =580, pady= 10,sticky = W)
    
#     late CXl input and labels
    Label(window, text= 'Late Cancellation',bg = labelBG, fg=labelFG, font=labelfont) .grid (row=6,column=0,padx = 25,sticky = W) 
    inputboxLateCxl = Entry(window, width = 4, bg=inputBG,fg=inputFG ,font = inputfont)
    inputboxLateCxl.grid(row = 6, column = 0,padx = 185, pady= 0, sticky = W)
    
    Label(window, text= 'Reason',bg = labelBG, fg=labelFG, font=labelfont) .grid (row=6,column=0, padx = 255,sticky = W) 
    inputboxLateCxlRs = Entry(window, width = 15, bg=inputBG,fg=inputFG ,font = inputfont)
    inputboxLateCxlRs.grid(row = 6, column = 0,padx =330, pady=10, sticky = W)
    
#     button for lateCxl submit
    LateCxlBUTT=Button(window, text='LateCxl',width = 6, background = 'gray36',fg='white',command = lateCxlEntry) .grid(row=6, column= 0,padx =515, pady= 10,sticky = W)
    lateView =Button(window, text='View',width = 6, command = lateView) .grid(row=6, column= 0,padx =580, pady= 10,sticky = W)
    

#   ARRIVED input and labels
    Label(window, text= 'Arrived',bg = labelBG, fg=labelFG, font=labelfont) .grid (row=7,column=0,padx =25,sticky = W) 
    inputboxArrvd = Entry(window, width = 4, bg=inputBG,fg=inputFG ,font = inputfont)
    inputboxArrvd.grid(row = 7, column = 0,padx = 100, pady= 10, sticky = W)
    
#   button for Arrival xsubmit
    ArrBUTT=Button(window, text='Arrived',width = 6, background = 'gray36',fg='white',command = ArrivedEntry) .grid(row=7, column= 0,padx =160, pady= 10,sticky = W)
    ArrView =Button(window, text='View',width = 6, command = arrView) .grid(row=7, column= 0,padx =225, pady= 10,sticky = W)
    
    
    def UndoRes():
        del walkDataVar[1:]
        del LateCXlDataVar[1:]
        del Arrived[1:]
        arrivals.clear()
        print(f'asfddffsfffafdasdfasdf {arrivals}')
        print(Inbound)
        for aaaaa in range(len(Inbound)):
            arrivals.append(Inbound[aaaaa])
        print(walkDataVar)
        print(LateCXlDataVar)
        print(Arrived)
        print(arrivals)
        entryMainPrinter()
    
    UndoRes=Button(window, text='RESET',fg='white',font='helvetica 10 italic',width = 9,background ='red',  command = UndoRes) .grid(row= 8, column= 0,padx=15, pady =0, sticky = E)

    Done=Button(window, text='Done',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue' ,command = fin) .grid(row= 8, column= 0,padx=25,pady =50, sticky = W)

    for a in range(len(Inbound)):
        arrivals.append(Inbound[a])

    entryMainPrinter()
    window.mainloop()

