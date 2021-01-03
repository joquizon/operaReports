from datetime import datetime
from datetime import date
from datetime import timedelta

import os
from xml.etree import ElementTree



# section for the title
# time data extratct
today = date.today()
audited = ((today - timedelta(days = 1)).strftime('%x'))
yesterday = ((today - timedelta(days = 1)).strftime('%A'))


# title Table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
title = [['The Maritime Hotel'],['Night Audit Report'],[yesterday], [audited]]

# stat Title table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
stattitle = ['STATISTICS']

# mgr xml data extract
# statistics table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<
statistics = [['Total Revenue'],['Total Rooms Reserved'],['% of Rooms Occupied'],['Opera CC Total']]

# Manager report
mgrx = 'mgr.xml'
mgrz = os.path.join('xmltut',mgrx)
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
ccx = 'cred.xml'
ccz = os.path.join('xmltut',ccx)
ccf = ElementTree.parse(ccz)
print(ccf)

cctotal = ccf.findall('R_CREDIT')
statistics[3].append(cctotal[0].text)



# detailed availability section 

# detailed av table >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
detailedavail = [['DETAILED AVAILABILITY as of',audited],['QBS'],['SJR'],['VIP'],['TOTAL']]

# detailed av xml data extract
detavx = 'detav.xml'
detavz = os.path.join('xmltut',detavx)
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


# special events entry function

# special evts table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
specevBox = [['Special events','Location']]

empty = ['None']
evtHead =['Special events','Location']    

choices=[]

def specEvQ():
    specev = input('were there special Events tonight? - type <y> or type <n>: ')
    if specev == 'y':
        eventLister()
    elif specev == 'n':
        specevBox.append(empty)
        print('Ok cool')
    else:
        print('y Or n only please')
        specEvQ()
            
def eventLister():

    
    def infosure():
        sure = input('is this correct - type <y> or type <n>: ')
        if sure == 'y':
            print('cool!')
        elif sure =='n':
            eventLister()
        else:
            infosure()
    specevlister = []        
    eventName = input('please list the name of the event or <*> if there are no events at all:')
    
    if eventName == '*':
        specEvQ()
    
    location = input('Please list the location of the event or * if you listed the wrong location : ')
    
    if location == '*':
        eventLister()
    print(f'event: {eventName} // location: {location}')
    
    infosure()

    specevlister.append(eventName)
    specevlister.append(location)
    specevBox.append(specevlister)


    def singler():
        for x in range (1,(len(specevBox))):
            print(f'{x}....{specevBox[x]}')
            choices.append(str(x))
        print(f'{len(specevBox)}....all')
        print(choices)

        allorNah = input('Type the no. of the wrong entry: ')
        E = allorNah in choices
        if allorNah == str(len(specevBox)):
            specevBox.clear()
            specevBox.append(evtHead)
            morevents()
        elif E is True:
            specevBox.pop(int(allorNah))
            print(specevBox)
            morevents()
        else:
            print('try again please')
            singler()
    
    def moreP():
        morepop =  input('any more - type <y> or type <n>:')
        if morepop == 'y':
            singler()
        elif morepop == 'n':
            print('great')
            print(specevBox)
        else:
            print('y Or n only please')
            moreP()
            
    def morevents():
        more = input('Anymore Events? - type <y> or type <n>: ')
        if more == 'y':
            eventLister()
        elif more == 'n':
            print(specevBox)
            sure = input('is this information correct - type <y> or type <n>: ')
            if sure == 'y':
                print('great')
            elif sure == 'n':
                if len(specevBox)>2:
                    singler()
                elif len(specevBox) == 2:
                    specevBox.clear()
                    specevBox.append(evtHead)
                    specEvQ()
            else:
                print('y Or n only please')
                morevents()
        else:
            print('y Or n only please')
            morevents()
    
    morevents()       
specEvQ()



# zero rate
# zero rate xml data extract

zerox = 'zero.xml'
zeroz = os.path.join('xmltut',zerox)
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

# taxExmpt = [['Tax Exempt','Room No.', '$Rate','Nights']]

taxx = 'taxexempt3.xml'
taxz = os.path.join('xmltut',taxx)
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
    




# for walks late check ins no shows, Arrivals are grabbed and user enters group per res and tells program which is walk res and late cxl res

arrx = 'arr3.xml'
arrz = os.path.join('xmltut',arrx)
arrf = ElementTree.parse(arrz)
print(arrf)


# arrival  No Show Res # # Nights Company Group Travel Agent
# this list gathers the arrivals
arrivals = [['Name', 'ResNo.','Nights','Company','Group','Travel Agent']]

arrRtefind = arrf.findall('LIST_G_GROUP_BY1/G_GROUP_BY1/LIST_G_RESERVATION/G_RESERVATION')
arrRte = 'LIST_G_GROUP_BY1/G_GROUP_BY1/LIST_G_RESERVATION/G_RESERVATION'

# function asks user to manually enter group of res
def groupEntry():
    groupQ = input('please enter the group this reservation belongs to or type <n> for none: ')
    if groupQ == 'n':
        groupListing.append('None')
    else:
        groupListing.append(groupQ)

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
    groupEntry()
    arrivalEntry.append(groupListing[0])
    
    arrivalEntry.append(travelAgent[0])
    arrivals.append(arrivalEntry)

print(arrivals)


# prompts user to designate walks and late cxl in arrivals

ResCheck = []

# walk table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
walkData = [['Walked','Res No.','Hotel','Company','Group','Travel Agent']]

# late cxl table>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LateCXlData = [['Late Cancellation','Res No.','Reason','Company','Group','Travel Agent']]

empty = [['None'],[''],[''],[''],[''],['']]
def ArrivalsPrnter():
    for Arco in range(1,len(arrivals)):
        print(f'{Arco} .... {arrivals[Arco][0]}')
        ResCheck.append(str(Arco))        

def walkerCheck():
    walkQ = input('Type the No. of the res. that was walked or <n> for None: ')
    walker = walkQ in ResCheck
    if walkQ == 'n':
        walkData.append(empty)
    elif walker is True:
        hotelQ = input('Enter Name of Hotel that the guest was walked to: ')
        arrivals[int(walkQ)][2] = hotelQ
        walkData.append(arrivals[int(walkQ)])
        arrivals.pop(int(walkQ))
    else:
        print('Nope Try again!')
        walkerCheck()



def LateCXlerCheck():
    LateCXlQ = input('Type the No. of the res. that was LateCXled or <n> for None: ')
    LateCXler = LateCXlQ in ResCheck
    if LateCXlQ == 'n':
        walkData.append(empty)
    elif LateCXler is True:
        reasonQ = input('Enter Name of reason that the guest was LateCXled to: ')
        arrivals[int(LateCXlQ)][2] = reasonQ
        LateCXlData.append(arrivals[int(LateCXlQ)])
        arrivals.pop(int(LateCXlQ))
    else:
        print('Nope Try again!')
        LateCXlerCheck()
        
ArrivalsPrnter()
walkerCheck()
print(walkData)
ArrivalsPrnter()
print(LateCXlData)
LateCXlerCheck()

ArrivalsPrnter()
Noshowdata = arrivals


