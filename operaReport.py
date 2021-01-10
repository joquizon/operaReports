
# program should be run after midnight
# user must log in
# program executes >>>>
# creates folder for xml files and pdf to be downloaded to manually
# creates data for cover page of final report
# title block dated previous day
# data gathered from xml forms
# ---- stats
# ---- det av
# ---- tax exempt
# ---- house use
# >>>>>>>>>>>>>>>>>>>>> Arrivals xml provides all arrivals. as loop goes through 
# >>>>>>>>>>>>>>>>>>>>> tkinter gui appears asks user for group listing 
# >>>>>>>>>>>>>>>>>>>>> User is asked which ones are walked late cxl or arrived 
# >>>>>>>>>>>>>>>>>>>>> any not sorted by user will be listed as no show
# ---- walked
# ---- late cxl
# ---- no show
# ---- forecast



from datetime import datetime
from datetime import date
from datetime import timedelta

import os
from xml.etree import ElementTree

import tkinter 
from tkinter import *
from tkinter import messagebox

from threading import Timer

from arrivalSorter import arrivalOPTs

from manualEntries import manuaQ


import PyPDF2
from PyPDF2 import PdfFileMerger

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.pagesizes import letter


# section for the title
# time data extratct
today = date.today()
audited = ((today - timedelta(days = 1)).strftime('%x'))
yesterday = ((today - timedelta(days = 1)).strftime('%A'))


# this list is utilized by groupentry function
groupListing = []


# this list is utilized by arrivals sorter and all manual arrival entrys
arrivalMain = [['Name', 'ResNo.','Nights','Company','Group','Travel Agent']]
Temprrvl = [['Name', 'ResNo.','Nights','Company','Group','Travel Agent']]
walkData = [['Walked','Res No.','Hotel','Company','Group','Travel Agent']]
LateCXlData = [['Late Cancellation','Res No.','Reason','Company','Group','Travel Agent']]

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

# created folder name
Targfold = ['x']


# set of list is used by filestarter function to check and assign filenames to vars
mgrxFile =  []
ccxFile =  []
detavxFile =  []
zeroxFile =  []
taxxFile =  []
arrxFile =  []
forecastxFile =  []

fileLocker=[mgrxFile,ccxFile,detavxFile,zeroxFile,taxxFile,arrxFile,forecastxFile]
fileLockerSTR=['mgrReport','CC report','det avail','zero rate','tax Exmpt','arrivals','forecast']

wtflist = []

MissXmlsList = []
MissPdflist = []

DupXmlsList = []
DupPdflist = []



gibyroom = []
guest = []
manager = []
resDet = []

pdfLocker =[guest,manager]
pdfLockerSTR =['guest','manager']

pdfLocker2 =[gibyroom,resDet]
pdfLockerSTR2 =['gibyroom','resDet']


# prompts user to enter full name
entryName = [[]]
def enterName():
    window = Tk()
    # creates title in window border
    window.title('OPERA Night Audit Manager Pack creator')
    window.configure(background ='white')
    window.geometry('235x175')

    def name(x):
        usergot = username.get()
        entryName[0].append(f'created by {usergot}')
        window.destroy()
    
    username = Entry(window, bg='gray64',fg=inputFG ,font = inputfont, justify = 'center')
    username.grid(row = 1, column = 0,padx =5, pady=20, sticky = N)
    
    lbl1 = Label (window, text='Enter\nFull Name\nplease ',bg = labelBG, fg='black', font='helvetica 15 italic')
    lbl1.grid (row = 0,column='0',padx = 5,pady=10, sticky = N)


    username.bind('<Return>',name)
    window.mainloop()
enterName()





# creates the folder names it of  date being audited...checks if it exists aND prompts user to save xml and pdf files to folder
def createFolder():
    
    def folderError():
        window = Tk()
        # creates title in window border
        window.title('OPERA Night Audit Manager Pack creator')
        window.configure(background ='white')
        window.geometry('150x250')

        def TryAgain():
            window.destroy()
            createFolder()
        lbl1 = Label (window, text=f'ERROR!!!\n{Targfold[0]}\nalready Exists!!!\nMove folder then\nClick Try Again',bg = labelBG, fg='black', font='helvetica 14 italic')
        lbl1.grid (row = 0,column='0',padx = 0,pady=5, sticky = N)

        tryagain=Button(window, text=f'TRY\nAgain',font='helvetica 12 italic',width = 9,height=4,background ='red',fg = 'white' ,command = TryAgain) .grid(row= 8, column= 0,padx=0,pady =5, sticky = N)

        window.mainloop()
    
    
    
    def folderMessage():
        window = Tk()
        # creates title in window border
        window.title('OPERA Night Audit Manager Pack creator')
        window.configure(background ='white')
        window.geometry('150x220')

        def start():
            window.destroy()
        lbl1 = Label (window, text= f'Download\nxml and pdf files\ninto folder\n{Targfold[0]}',bg = labelBG, fg='black', font='helvetica 14 italic')
        lbl1.grid (row = 0,column='0',padx = 0,pady=5, sticky = N)

        start=Button(window, text=f'Files\nReady',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue',fg='white' ,command = start) .grid(row= 8, column= 0,padx=0,pady =5, sticky = N)

        window.mainloop()
    
    
    today = date.today()
    audited = ((today - timedelta(days = 1)).strftime('%x'))
    directory = audited.replace('/','')
    Targfold[0] = directory
    already = os.path.exists(directory)
    if already is False:
        os.makedirs(directory)
        folderMessage()
    else:
        print('Error!check folder names')
        folderError()


createFolder()


# this checks the folder created and checks if user has the correct files in folder
def fileStarter():
	filesContained = os.listdir(Targfold[0])

	def fileMiss():
		window = Tk()
		window.title('OPERA Night Audit Manager Pack creator')
		window.configure(background ='white')        
		window.geometry('500x500')
		Label (window, text=f'{len(MissXmlsList)} issues ...{MissXmlsList}',bg = labelBG, fg='violet red', font='helvetica 12') .grid (row = 1,column='0',padx = 20,pady=0, sticky = W)
		Label (window, text=f'{len(DupXmlsList)} issues ...{DupXmlsList}',bg = labelBG, fg='violet red', font='helvetica 12') .grid (row = 2,column='0',padx = 20,pady=0, sticky = W)
		Label (window, text=f'{len(MissPdflist)} issues ...{MissPdflist}',bg = labelBG, fg='purple3', font='helvetica 12') .grid (row = 3,column='0',padx = 20,pady=0, sticky =W)
		Label (window, text=f'{len(DupPdflist)} issues ...{DupPdflist}',bg = labelBG, fg='purple3', font='helvetica 12') .grid (row = 4,column='0',padx = 20,pady=0, sticky = W)


		def start():
			MissXmlsList.clear()
			MissPdflist.clear()
			DupXmlsList.clear()
			DupPdflist.clear()
			window.destroy()
			fileStarter()
		lbl1 = Label (window, text=f'!!!!!!!!\nFILE MISSING IN\n{Targfold[0]}\nMissing contents:',bg = labelBG, fg='black', font='helvetica 14 italic')
		lbl1.grid (row = 0,column='0',padx = 20,pady=5, sticky = W)

		start=Button(window, text=f'Files\nReady',font='helvetica 12 italic',width = 9,height=4,background ='dodger blue' ,command = start) .grid(row= 30, column= 0,padx=20,pady =20, sticky = W)

		window.mainloop()

	for file in range(len(filesContained)):
		if filesContained[file].startswith('man') and filesContained[file].endswith('xml'):
			mgrxFile.append(filesContained[file])
		elif filesContained[file].startswith('fin'):
			ccxFile.append(filesContained[file])
		elif filesContained[file].startswith('det'):
			detavxFile.append(filesContained[file])
		elif filesContained[file].startswith('gi_'):
			zeroxFile.append(filesContained[file])
		elif filesContained[file].startswith('tax'):
			taxxFile.append(filesContained[file])
		elif filesContained[file].startswith('res') and filesContained[file].endswith('xml'):
			arrxFile.append(filesContained[file])
		elif filesContained[file].startswith('his'):
			forecastxFile.append(filesContained[file])
		elif filesContained[file].startswith('man') and filesContained[file].endswith('pdf'):
			manager.append(filesContained[file])
		elif filesContained[file].startswith('res') and filesContained[file].endswith('pdf'):
			resDet.append(filesContained[file])
		elif filesContained[file].startswith('giby'):
			gibyroom.append(filesContained[file])
		elif filesContained[file].startswith('guest'):
			guest.append(filesContained[file])
		else:
			wtf.append(filesContained[file])

	print(fileLocker)
	print(pdfLocker)
	print(pdfLocker2)

	for seek in range(len(fileLocker)):
		if len(fileLocker[seek]) == 0:
			MissXmlsList.append(f'missing {fileLockerSTR[seek]} XML file in folder !!!')
			print('missing XML file')
		elif len(fileLocker[seek]) >1:
			DupXmlsList.append(f'more than 1 {fileLockerSTR[seek]} XML  file in folder !!! ')
			print(f'more than 1 {fileLockerSTR[seek]} XML  file in folder ')
		else:
			pass

	for seekp in range(len(pdfLocker)):
		if len(pdfLocker[seekp]) == 0:
			MissPdflist.append(f'missing {pdfLockerSTR[seekp]} PDF file in folder !!!')
			print(f'missing {pdfLockerSTR[seekp]} PDF file in folder')
		elif len(pdfLocker[seekp])> 1:
			DupPdflist.append(f'more than 1 {pdfLockerSTR[seekp]} PDF file in folder !!!')
			print(f'more than 1 {pdfLockerSTR[seekp]} PDF file in folder')
		else:
			pass

	for seekd in range(len(pdfLocker2)):
		if len(pdfLocker2[seekd]) < 2:
			MissPdflist.append(f'missing {pdfLockerSTR2[seekd]} PDF file in folder !!!')
			print(f'missing {pdfLockerSTR2[seekd]} PDF file in folder')
		elif len(pdfLocker2[seekd])> 2:
			DupPdflist.append(f' More than 2 {pdfLockerSTR2[seekd]} PDF file in folder !!!')
			print(f'More than 2 {pdfLockerSTR2[seekd]} PDF file in folder')
		else:
			pass
	print(MissPdflist)
	print(MissXmlsList)
	print(DupXmlsList)
	print(DupPdflist)

	if len(MissXmlsList)>0 or len(DupXmlsList)>0 or len(MissPdflist)>0 or len(DupPdflist)>0:
		mgrxFile.clear()
		ccxFile.clear()
		detavxFile.clear()
		zeroxFile.clear()
		taxxFile.clear()
		arrxFile.clear()
		forecastxFile.clear()
		gibyroom.clear()
		guest.clear()
		manager.clear()
		resDet.clear()
		fileMiss()
	else:
		print(fileLocker)
		print(pdfLocker)
		print(pdfLocker2)
		print("all's gravy baby!")
fileStarter()



# title Table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
title = [['The Maritime Hotel'],['Night Audit Report'],[f'{yesterday} {audited}']]

# stat Title table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stattitle = [['STATISTICS']]

# mgr xml data extract
# statistics table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<
statistics = [['Total Revenue'],['Total Rooms Reserved'],['% of Rooms Occupied'],['Opera CC Total']]

# Manager report
mgrx = mgrxFile[0]
mgrz = os.path.join(Targfold[0],mgrx)
mgrf = ElementTree.parse(mgrz)
print(mgrf)


linefind = mgrf.findall('LIST_G_MASTER_VALUE_ORDER/G_MASTER_VALUE_ORDER/LIST_G_LAST_YEAR_01/G_LAST_YEAR_01/LIST_G_CROSS/G_CROSS/LIST_G_MASTER_VALUE/G_MASTER_VALUE/SUB_GRP_1_ORDER')

for lf in range(0,99):
    if linefind[lf].text == '30000':
        mroute = mgrf.findall(f'LIST_G_MASTER_VALUE_ORDER/G_MASTER_VALUE_ORDER/LIST_G_LAST_YEAR_01/G_LAST_YEAR_01/LIST_G_CROSS/G_CROSS/LIST_G_MASTER_VALUE/G_MASTER_VALUE[{lf}]/LIST_G_HEADING_1_ORDER/G_HEADING_1_ORDER/LIST_G_SUM_AMOUNT/G_SUM_AMOUNT/SUM_AMOUNT')
#         total rooms
        statistics[1].append(mroute[0].text)
#     elif linefind[lf].text == '80000':
#         mroute = mgrf.findall(f'LIST_G_MASTER_VALUE_ORDER/G_MASTER_VALUE_ORDER/LIST_G_LAST_YEAR_01/G_LAST_YEAR_01/LIST_G_CROSS/G_CROSS/LIST_G_MASTER_VALUE/G_MASTER_VALUE[{lf}]/LIST_G_HEADING_1_ORDER/G_HEADING_1_ORDER/LIST_G_SUM_AMOUNT/G_SUM_AMOUNT/SUM_AMOUNT')
#         print(f'House Use {mroute[0].text}')
    elif linefind[lf].text == '860000':
        mroute = mgrf.findall(f'LIST_G_MASTER_VALUE_ORDER/G_MASTER_VALUE_ORDER/LIST_G_LAST_YEAR_01/G_LAST_YEAR_01/LIST_G_CROSS/G_CROSS/LIST_G_MASTER_VALUE/G_MASTER_VALUE[{lf}]/LIST_G_HEADING_1_ORDER/G_HEADING_1_ORDER/LIST_G_SUM_AMOUNT/G_SUM_AMOUNT/SUM_AMOUNT')
        statistics[0].append(mroute[0].text)
    elif linefind[lf].text == '300000':
        mroute = mgrf.findall(f'LIST_G_MASTER_VALUE_ORDER/G_MASTER_VALUE_ORDER/LIST_G_LAST_YEAR_01/G_LAST_YEAR_01/LIST_G_CROSS/G_CROSS/LIST_G_MASTER_VALUE/G_MASTER_VALUE[{lf}]/LIST_G_HEADING_1_ORDER/G_HEADING_1_ORDER/LIST_G_SUM_AMOUNT/G_SUM_AMOUNT/SUM_AMOUNT')
        statistics[2].append(f'{mroute[0].text}%')
    else:
        pass

# credit cards total appends to statistics table>>>>>>>>>>>>>>>>>>
# credit cards total xml data extract
ccx = ccxFile[0]
ccz = os.path.join(Targfold[0],ccx)
ccf = ElementTree.parse(ccz)
print(ccf)

cctotal = ccf.findall('R_CREDIT')
statistics[3].append(cctotal[0].text)



# detailed availability section 

# detailed av table >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
detailedavail = [['DETAILED AVAILABILITY as of',audited],['QBS'],['SJR'],['VIP'],['TOTAL']]

# detailed av xml data extract
detavx = detavxFile[0]
detavz = os.path.join(Targfold[0],detavx)
detavf = ElementTree.parse(detavz)
print(detavf)

detroute = 'LIST_G_5/G_5/LIST_DAY/DAY[1]/'
dater = detavf.findall(f'{detroute}BUSINESS_DATE')

numeros = []
for zz in range(1,6):
    subdetroute = f'{detroute}LIST_ROOM_TYPE/ROOM_TYPE'
    numrooms = detavf.findall(f'{subdetroute}{[zz]}/LIST_DETAIL/DETAIL/NO_OF_ROOMS1')
    numeros.append(int(numrooms[0].text))

qbs = str(numeros[0] + numeros[-1])
vip = str(numeros[2] + numeros[3])

detailedavail[1].append(qbs)
detailedavail[2].append(numeros[1])
detailedavail[3].append(vip)
detailedavail[4].append(sum(numeros))




# zero rate
# zero rate xml data extract

zerox = zeroxFile[0]
zeroz = os.path.join(Targfold[0],zerox)
zerof = ElementTree.parse(zeroz)
print(zerof)

# zero rate table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
zeroRateRooms = [['House Use and Comp Use','Room No.', 'Nights']]

roomhold = zerof.findall('LIST_G_ROOM/G_ROOM')
for zr in range(1,(len(roomhold)+1)):
    zeroroute = f'LIST_G_ROOM/G_ROOM[{zr}]'
    roomno = zerof.findall(f'{zeroroute}/ROOM')
    arrdate = zerof.findall(f'{zeroroute}/ARR')
    depdate = zerof.findall(f'{zeroroute}/DEP')
    guest = zerof.findall(f'{zeroroute}/GUEST_NAME')
    
    strArrdate = arrdate[0].text
    arrdateM = strArrdate[0]+strArrdate[1]
    arrdateD = strArrdate[3]+strArrdate[4]
    arrdateY = strArrdate[6]+strArrdate[7]
    
    strDepdate = depdate[0].text
    DepdateM = strDepdate[0]+strDepdate[1]
    DepdateD = strDepdate[3]+strDepdate[4]
    DepdateY = strDepdate[6]+strDepdate[7]
    
    from datetime import datetime
    date_format = "%m/%d/%Y"
    a = datetime.strptime(f'{arrdateM}/{arrdateD}/20{arrdateY}', date_format)
    b = datetime.strptime(f'{DepdateM}/{DepdateD}/20{DepdateY}', date_format)
    delta = b-a
    
    houseUseEntry = []
    houseUseEntry.append(guest[0].text)
    houseUseEntry.append(roomno[0].text)
    houseUseEntry.append(delta.days)
    
    zeroRateRooms.append(houseUseEntry)

    print(f'Guest {roomno[0].text} // {guest[0].text}')
    print (f'No.of nights {delta.days}\n')



# tax exempt xml data extract
# Tax Exempt Room# $Rate #Nights


taxx = taxxFile[0]
taxz = os.path.join(Targfold[0],taxx)
taxf = ElementTree.parse(taxz)
print(taxf)

# Tax Exempt table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
taxExmpt = [['Tax Exempt','Room No.', '$Rate','Nights']]

rtefind = taxf.findall('LIST_G_GROUP_BY_STATUS/G_GROUP_BY_STATUS/LIST_G_NAME_TAX_DESCRIPTION/G_NAME_TAX_DESCRIPTION/LIST_G_RESV_NAME_ID/G_RESV_NAME_ID')
taxrte = 'LIST_G_GROUP_BY_STATUS/G_GROUP_BY_STATUS/LIST_G_NAME_TAX_DESCRIPTION/G_NAME_TAX_DESCRIPTION/LIST_G_RESV_NAME_ID/G_RESV_NAME_ID'
print(len(rtefind))


for taxer in range(1,((len(rtefind))+1)):
    taxEntry = []
    name = taxf.findall(f'{taxrte}[{taxer}]/FULL_NAME')
    taxEntry.append(name[0].text)
    roomno = taxf.findall(f'{taxrte}[{taxer}]/ROOM')
    taxEntry.append(roomno[0].text)
    rate= taxf.findall(f'{taxrte}[{taxer}]/RATE_AMOUT')
    taxEntry.append(f'${rate[0].text}')
    Adate = taxf.findall(f'{taxrte}[{taxer}]/ARRIVAL')
    Ddate = taxf.findall(f'{taxrte}[{taxer}]/DEPARTURE')
    
    strArrdate = Adate[0].text
    arrdateM = strArrdate[0]+strArrdate[1]
    arrdateD = strArrdate[3]+strArrdate[4]
    arrdateY = strArrdate[6]+strArrdate[7]
    
    strDepdate = Ddate[0].text
    DepdateM = strDepdate[0]+strDepdate[1]
    DepdateD = strDepdate[3]+strDepdate[4]
    DepdateY = strDepdate[6]+strDepdate[7]
    
    from datetime import datetime
    date_format = "%m/%d/%Y"
    a = datetime.strptime(f'{arrdateM}/{arrdateD}/20{arrdateY}', date_format)
    b = datetime.strptime(f'{DepdateM}/{DepdateD}/20{DepdateY}', date_format)
    delta = b-a
    
    taxEntry.append(f'{delta.days} Nights')
    taxExmpt.append(taxEntry)
    





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
            window.after(10,window.destroy)
            print(groupListing)

        else:
            groupListing.append(entered_text)
            answer.delete(0,END)
            lbl2['text']= f'ok cool'
            window.after(10,window.destroy)
            print(groupListing)
        
    lbl2 = Label (window, text='',bg = labelBG, fg='red', font=labelfont)
    lbl2.grid (row = 2,column='0', sticky = N)
    answer.bind('<Return>',response)
    
    window.mainloop()




# for walks late check ins no shows, Arrivals are grabbed and user enters group per res and tells program which is walk res and late cxl res

arrx = arrxFile[0]
arrz = os.path.join(Targfold[0],arrx)
arrf = ElementTree.parse(arrz)
print(arrf)





arrRtefind = arrf.findall('LIST_G_GROUP_BY1/G_GROUP_BY1/LIST_G_RESERVATION/G_RESERVATION')
arrRte = 'LIST_G_GROUP_BY1/G_GROUP_BY1/LIST_G_RESERVATION/G_RESERVATION'

# arrival  No Show Res # # Nights Company Group Travel Agent
# this list gathers the arrivals
# arrival  No Show Res # # Nights Company Group Travel Agent

arrRtefind = arrf.findall('LIST_G_GROUP_BY1/G_GROUP_BY1/LIST_G_RESERVATION/G_RESERVATION')
arrRte = 'LIST_G_GROUP_BY1/G_GROUP_BY1/LIST_G_RESERVATION/G_RESERVATION'



z = len(arrRtefind)
for arr in range(1,(z+1)):
    arrivalEntry = []
    ArrName = arrf.findall(f'{arrRte}[{arr}]/FULL_NAME')
    arrivalEntry.append(ArrName[0].text)
    
    ResNo = arrf.findall(f'{arrRte}[{arr}]/CONFIRMATION_NO')
    arrivalEntry.append(ResNo[0].text)
    
    Arridate = arrf.findall(f'{arrRte}[{arr}]/ARRIVAL')
    Deprdate = arrf.findall(f'{arrRte}[{arr}]/DEPARTURE')
    
    strArrdate = Arridate[0].text
    arrdateM = strArrdate[0]+strArrdate[1]
    arrdateD = strArrdate[3]+strArrdate[4]
    arrdateY = strArrdate[6]+strArrdate[7]
    
    strDepdate = Deprdate[0].text
    DepdateM = strDepdate[0]+strDepdate[1]
    DepdateD = strDepdate[3]+strDepdate[4]
    DepdateY = strDepdate[6]+strDepdate[7]
    
    from datetime import datetime
    date_format = "%m/%d/%Y"
    a = datetime.strptime(f'{arrdateM}/{arrdateD}/20{arrdateY}', date_format)
    b = datetime.strptime(f'{DepdateM}/{DepdateD}/20{DepdateY}', date_format)
    delta = b-a
    
    NightNo = (f'{delta.days} Nights')
    arrivalEntry.append(NightNo)
    
    companyFind = arrf.findall(f'{arrRte}[{arr}]/COMPANY_NAME')
    companylistingF = companyFind[0].text
    companylisting = companylistingF.replace('\n','')
    
    companyEntry = []
    travelAgent = []
    
    if 'C-' in (companylisting) and 'T-' not in (companylisting):
        xco = companylisting.replace('C- ','')
        companyEntry.append(xco)
        print(companyEntry)
    elif 'C-' not in (companylisting) and 'T-' in (companylisting):
        xta = companylisting.replace('T- ','')
        travelAgent.append(xta)
        print(travelAgent)
    elif 'C-' and 'T-' in (companylisting):
        for cc in range(len(companylisting)):
            if companylisting[cc-1] + companylisting[cc]== 'T-':
                x = (cc-1)
                companyword = []
                travelword = []
                for dd in range(3,x):    
                    companyword.append(companylisting[dd])
                for ee in range(x+3,(len(companylisting))):
                    travelword.append(companylisting[ee])
            else:
                pass
        companyEntry.append(''.join(companyword))
        travelAgent.append(''.join(travelword))
    else:
        companyEntry.append('None')
        travelAgent.append('None')
    arrivalEntry.append(companyEntry[0])
    
    groupListing = []
    print(f'Reservation: {ArrName[0].text}')
    # >>>>>>>>>>>>>>>>>>>>>>>>>>groupentry func is called in this loop>>>>>>>>>>>>>>
    groupEntry()
    arrivalEntry.append(groupListing[0])
    
    arrivalEntry.append(travelAgent[0])
    arrivalMain.append(arrivalEntry)
    Temprrvl.append(arrivalEntry)

# this function asks User to sort out wether arrivals listed rare walks late cxl or no show or if anyone on list has already arrived 
arrivalOPTs(arrivalMain,walkData,LateCXlData)
print(arrivalMain)
# this function asks User if any Noshows need to be manually entered
manuaQ(arrivalMain,walkData,LateCXlData)
print(arrivalMain)






#Forecast xml data extract

forecasttitle = ['Forecast for the following 7 Days']



# hist and forec data
forecastx = forecastxFile[0]
forecastz = os.path.join(Targfold[0],forecastx)
forecastf = ElementTree.parse(forecastz)
print(forecastf)


# Date Occupancy RMS RSVD Arrivals Departures Avg. Rate
mainForecastList = [['Date',' Occupancy','RMS','RSVD','Arrivals','Departures','Avg. Rate']]

for x in range(2,9):
    forecastentry = []
    route = f'LIST_G_GPAGEID/G_GPAGEID/LIST_G_REC_TYPE/G_REC_TYPE[2]/LIST_G_CONSIDERED_DATE/G_CONSIDERED_DATE[{x}]/'
    dates = forecastf.findall(f'{route}CHAR_CONSIDERED_DATE')
    occ = forecastf.findall(f'{route}CF_OCCUPANCY')
    rmsres = forecastf.findall(f'{route}NO_ROOMS')
    arrs = forecastf.findall(f'{route}ARRIVAL_ROOMS')
    deps = forecastf.findall(f'{route}DEPARTURE_ROOMS')
    avgr = forecastf.findall(f'{route}CF_AVERAGE_ROOM_RATE')
    
    
    for c in dates:
        forecastentry.append(c.text)

    for d in occ:
        forecastentry.append(f'{d.text}%')

    for e in rmsres:
        forecastentry.append(e.text)

    for f in arrs:
        forecastentry.append(f.text)

    for g in deps:
        forecastentry.append(g.text)

    for h in deps:
        forecastentry.append(h.text)
        
    for i in avgr:
        forecastentry.append(f'${i.text}')
    mainForecastList.append(forecastentry)






print(title)
print(entryName)
print(stattitle)
print(statistics )
print(detailedavail)
print(zeroRateRooms)
print(walkData)
print(LateCXlData)
print(arrivalMain)
print(mainForecastList)