

# asks users if they need to manually enter a no show res
def manualNoShowQ():
    window = Tk()
    # creates title in window border
    window.title('OPERA Night Audit Manager Pack creator')
    window.configure(background ='white')
    window.geometry('400x200')

    def yes():
        print('yes')
        window.destroy()
        manualNOshowEntry()

    def no():
        print('no')
        lbl2['text']= f'ok cool'
        window.after(1000,window.destroy)
            
    
    lbl1 = Label (window, text='Do you need to manually enter a no show?',bg = labelBG, fg='black', font='helvetica 15 italic')
    lbl1.grid (row = 0,column='0',padx = 5,pady=10, sticky = W)
       
    lbl2 = Label (window, text='',bg = labelBG, fg='red', font=labelfont)
    lbl2.grid (row = 2,column='0',padx = 5,pady=0, sticky = N)
    
    Button(window, text='Yes',font='helvetica 10 italic',width = 9,height=4,background ='dodger blue',  command = yes) .grid(row= 8, column= 0,padx=25, pady =0, sticky = W)

    Button(window, text='No',fg='white',font='helvetica 10 italic',width = 9,height=4,background ='red' ,command = no) .grid(row= 8, column= 0,padx=25,pady =0, sticky = E)

    window.mainloop()
















# allows user to manually enter no shows

def manualNOshowEntry():
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
        
        


    window = Tk()
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
    
    def click2():
        print('clicked~~~')
        for et in range(len(entryMain)):
            arrivalsMain.append(entryMain[et])
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
    
    btn2=Button(window, text='Done',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue', command = click2) .grid(row= 9, padx=25, column= 0, sticky = W)

    window.mainloop()



