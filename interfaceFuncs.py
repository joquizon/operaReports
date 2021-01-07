import tkinter 
from tkinter import *
from threading import Timer



# function allows user to enter group name for each reservation as application loops through xml data
def groupEntry():
    window = Tk()
    # creates title in window border
    window.title('OPERA Night Audit Manager Pack creator')
    window.configure(background ='white')
    window.geometry('400x200')
    
    lbl1 = Label (window, text='please enter group name for res or hit <enter> for none: ',bg = labelBG, fg=labelFG, font=labelfont)
    lbl1.grid (row = 0,column='0', sticky = N)
    
    answer = Entry(window, width = 20, bg=inputBG,fg=inputFG ,font = inputfont, justify = 'center')
    answer.grid(row = 1, column = 0,padx = paddingX, pady= paddingY, sticky = N)
    
    def response(a):
        entered_text = answer.get()
        if entered_text == '':
            groupListing.append('None')
            lbl2['text']= f'None Entered'
            window.after(1000,window.destroy)
            print(groupListing)

        else:
            groupListing.append(entered_text)
            answer.delete(0,END)
            lbl2['text']= f'ok cool'
            window.after(1000,window.destroy)
            print(groupListing)
        
    lbl2 = Label (window, text='',bg = labelBG, fg='red', font=labelfont)
    lbl2.grid (row = 2,column='0', sticky = N)
    answer.bind('<Return>',response)
    
    window.mainloop()







# this function asks user if  any of the arrivals are no show / late cxl / walks
def arrivalOPTs():
    arrivals
    walksChoice = ['y']
    walksHotel = ['y1']
    
    lateCXLchoice = ['x']
    lateCXLreason = ['x1']

    arrivedChoice = ['z']
    
    window = Tk()
    # creates title in window border
    window.title('OPERA Night Audit Manager Pack creator')
    window.configure(background ='white')
    window.geometry('1920x400')

    def reset():
        del arrivals[1:]
        del walkData[1:]
        del LateCXlData[1:]
        del Arrived[1:]
        for aa in range(1,len(arrivalsMain)):
            arrivals.append(arrivalsMain[aa])
        print(walkData)
        print(LateCXlData)
        print(Arrived)
        print(arrivals)
        entryMainPrinter()
        

    def entryMainPrinter():
        output.delete(0.0,END)
        for x in range (1,len(arrivals)):
            output.insert(END,f'\nENTRY: {x}__________')
            for y in range(len(arrivals[x])):
                output.insert(END,f'  {arrivals[0][y]} / {arrivals[x][y]}     ')
    
    def entryWalkPrinter():
        output.delete(0.0,END)
        for x in range (1,len(walkData)):
            output.insert(END,f'\nWALKED: {x}__________')
            for y in range(len(walkData[x])):
                output.insert(END,f'  {walkData[0][y]} / {walkData[x][y]}     ')
    
    def entryLateCxlPrinter():
        output.delete(0.0,END)
        for x in range (1,len(LateCXlData)):
            output.insert(END,f'\nLate CXL: {x}__________')
            for y in range(len(LateCXlData[x])):
                output.insert(END,f'  {LateCXlData[0][y]} / {LateCXlData[x][y]}     ')
    
    def entryArrPrinter():
        output.delete(0.0,END)
        for x in range (1,len(Arrived)):
            output.insert(END,f'\nARRIVED: {x}__________')
            for y in range(len(Arrived[x])):
                output.insert(END,f'  {Arrived[0][y]} / {Arrived[x][y]}     ')        

    def walkEntry():
        print('walker')
        walkE = int(inputboxWalk.get())
        inputboxWalk.delete(0,END)
        walksChoice[0] = walkE
        print(walksChoice[0])
        walkTo = inputboxWalkRs.get()
        inputboxWalkRs.delete(0,END)
        arrivals[walkE][2] = walkTo
        walkData.append(arrivals[walkE])
        arrivals.pop(walkE)
        print(walkData)
        print(arrivals)
        entryWalkPrinter()
        w = Timer(4, entryMainPrinter)
        w.start()
        
    def walkView():
        entryWalkPrinter()
        w = Timer(8, entryMainPrinter)
        w.start()

    def lateView():
        entryLateCxlPrinter()
        l = Timer(8, entryMainPrinter)
        l.start()
        
    def arrView():
        entryArrPrinter()
        a = Timer(8, entryMainPrinter)
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
        LateCXlData.append(arrivals[lateE])
        arrivals.pop(lateE)
        print(LateCXlData)
        print(arrivals)
        entryLateCxlPrinter()
        l = Timer(4, entryMainPrinter)
        l.start()
        
    
    
    def ArrivedEntry():
        print('arred')
        arrPop = int(inputboxArrvd.get())
        inputboxArrvd.delete(0,END)
        Arrived.append(arrivals[arrPop])
        arrivals.pop(arrPop)
        entryArrPrinter()
        a = Timer(4, entryMainPrinter)
        a.start()        

        
    def fin():
        print('clicked~~~finito')
        arrivalsMain.clear()
        for bb in range(len(arrivals)):
            arrivalsMain.append(arrivals[bb])
        print(arrivalsMain)
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
    
    
    
    
    Reset=Button(window, text='Reset',fg='white',font='helvetica 10 italic',width = 9,background ='red',  command = reset) .grid(row= 8, column= 0,padx=15, pady =0, sticky = E)

    Done=Button(window, text='Done',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue' ,command = fin) .grid(row= 8, column= 0,padx=25,pady =50, sticky = W)

    
    entryMainPrinter()
    window.mainloop()



    