import PyPDF2
from PyPDF2 import PdfFileMerger

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Table
from reportlab.lib.pagesizes import letter


from reportlab.platypus import TableStyle
from reportlab.lib import colors


from arrivalSorter import arrivalOPTs
from manualEntries import manuaQ



# this function takes the lists populated in operReport funcs and creates Tables for pdf 
def coverCreate(dirVAR,titleVAR,entryNameVAR,stattitleVAR,statisticsVAR,detavTitleVAR,detailedavailVAR,taxExmptVAR,zeroRateRoomsVAR,walkDataVAR,LateCXlDataVAR,arrivalMainVAR,mainForecastListVAR):
	elements =[]


# this is the title of the file created by this function
	cover = f'{dirVAR}/coverpage for {dirVAR}.pdf'

	pdf = SimpleDocTemplate(cover,pagesize = letter, topMargin= 15,bottomMargin= 10, leftMargin = 20, rightMargin =20 )

	titleVAR= Table(titleVAR,colWidths=550,hAlign='CENTER')
	entryNameVAR= Table(entryNameVAR,hAlign='LEFT')
	stattitleVAR= Table(stattitleVAR,hAlign='LEFT')
	statisticsVAR= Table(statisticsVAR,hAlign='LEFT', colWidths =(125) )
	detavTitleVAR= Table(detavTitleVAR,hAlign='LEFT' )
	detailedavailVAR= Table(detailedavailVAR,hAlign='LEFT', colWidths =(100))
	taxExmptVAR= Table(taxExmptVAR,hAlign='LEFT', colWidths=(125))
	zeroRateRoomsVAR= Table(zeroRateRoomsVAR,hAlign='LEFT')
	walkDataVAR= Table(walkDataVAR,hAlign='LEFT', colWidths=(125))
	LateCXlDataVAR= Table(LateCXlDataVAR,hAlign='LEFT', colWidths=(125))
	arrivalMainVAR= Table(arrivalMainVAR,hAlign='LEFT', colWidths=(125))
	mainForecastListVAR= Table(mainForecastListVAR,hAlign='LEFT')


	elements.append(titleVAR)
	elements.append(entryNameVAR)
	elements.append(stattitleVAR)
	elements.append(statisticsVAR)
	elements.append(detavTitleVAR)
	elements.append(detailedavailVAR)
	elements.append(taxExmptVAR)
	elements.append(zeroRateRoomsVAR)
	elements.append(walkDataVAR)
	elements.append(LateCXlDataVAR)
	elements.append(arrivalMainVAR)
	elements.append(mainForecastListVAR)
	    


	formatTitle = TableStyle([
	    ('BACKGROUND', (0,0), (0,-1), colors.lightgrey),
	    ('TEXTCOLOR',(0,0),(0,-1),colors.blue),
	    ('ALIGN',(0,0),(0,-1),'CENTER'),
	    
	    ('FONTNAME',(0,0),(0,-1), 'Helvetica-Bold'),
	    ('FONTSIZE',(0,0),(0,-1), 27),
	    
	    ('BOTTOMPADDING',(0,0),(0,-1),18)
	])

	titleVAR.setStyle(formatTitle)


	formatName = TableStyle([
	    ('TEXTCOLOR',(0,0),(0,-1),colors.black),
	    ('ALIGN',(0,0),(0,-1),'LEFT'),
	    
	    ('FONTNAME',(0,0),(0,-1), 'Helvetica'),
	    ('FONTSIZE',(0,0),(0,-1), 12),
	    ('TOPPADDING',(0,0),(0,-1),10)
	    
	])

	entryNameVAR.setStyle(formatName)

	formatStattit = TableStyle([
	    ('TEXTCOLOR',(0,0),(0,-1),colors.black),
	    ('ALIGN',(0,0),(0,-1),'LEFT'),
	    
	    ('FONTNAME',(0,0),(0,-1), 'Helvetica-Bold'),
	    ('FONTSIZE',(0,0),(0,-1),13),
	    
	])

	stattitleVAR.setStyle(formatStattit)




	formatStat =TableStyle([

	    ('ALIGN',(1,0),(1,-1),'CENTER'),
	    ('FONTNAME',(0,0),(0,3), 'Helvetica-Bold'),
	])

	statisticsVAR.setStyle(formatStat)






	formatDetavtit = TableStyle([
	    ('TEXTCOLOR',(0,0),(0,-1),colors.black),
	    ('ALIGN',(0,0),(0,-1),'LEFT'),
	    
	    ('FONTNAME',(0,0),(0,-1), 'Helvetica-Bold'),
	    ('FONTSIZE',(0,0),(0,-1), 12),
	    ('TOPPADDING',(0,0),(0,-1),5)
	    
	])

	detavTitleVAR.setStyle(formatDetavtit)


	formatDetav =TableStyle([

	    ('ALIGN',(1,0),(1,-1),'CENTER'),
	    ('FONTNAME',(0,0),(0,3), 'Helvetica-Bold'),
	])

	detailedavailVAR.setStyle(formatDetav)



	formatTaxEx =TableStyle([
	    ('TOPPADDING',(0,0),(3,0),10),
	    ('FONTNAME',(0,0),(3,0), 'Helvetica-Bold'),
	])

	taxExmptVAR.setStyle(formatTaxEx)


	formatZero =TableStyle([
	    ('TOPPADDING',(0,0),(3,0),5),
	    ('FONTNAME',(0,0),(3,0), 'Helvetica-Bold'),
	    ('BOTTOMPADDING',(0,-1),(3,-1),10),
	])

	zeroRateRoomsVAR.setStyle(formatZero)


	formatwalkData =TableStyle([
	    ('TOPPADDING',(0,0),(5,0),5),
	    ('FONTNAME',(0,0),(5,0), 'Helvetica-Bold'),
	])

	walkDataVAR.setStyle(formatwalkData)
	LateCXlDataVAR.setStyle(formatwalkData)
	arrivalMainVAR.setStyle(formatwalkData)

	formatForecast =TableStyle([
	    ('TOPPADDING',(0,0),(6,0),10),
	    ('FONTNAME',(0,0),(6,0), 'Helvetica-Bold'),
	    ('FONTSIZE',(0,0),(6,0), 12),
	])

	mainForecastListVAR.setStyle(formatForecast)

	pdf.build(elements)












import os

def report_merger(source_dir):
    print(source_dir)
    merger = PdfFileMerger()
    pdfSort = ['x','x','x','x','x','x','x']
    subRes = []
    subGib = []
    
    for item in os.listdir(source_dir):
        if item.endswith('pdf'):
            if item.startswith('cover'):
                pdfSort[0]=item
            elif item.startswith('man'):
                pdfSort[1]=item
            elif item.startswith('cover'):
                pdfSort[2]=item
            elif item.startswith('res'):
                subRes.append(item)
            elif item.startswith('gib'):
                subGib.append(item)
            elif item.startswith('guest'):
                pdfSort[5] = item
            else:
                pass
        else:
            pass
    print(pdfSort)
    print(subRes)
    print(subGib)
    if int(subRes[0][-8:-4])<int(subRes[1][-8:-4]):
        pdfSort[2] = subRes[0]
        pdfSort[3] = subRes[1]
    else:
        print("Opera Naming element change check opera filenames")
    
    if int(subGib[0][-8:-4])<int(subGib[1][-8:-4]):
        pdfSort[6] = subGib[0]
        pdfSort[4] = subGib[1]
    else:
        print("Opera Naming element change check opera filenames")
    
    print(pdfSort)
    
    for new in range(len(pdfSort)):
        os.rename(f'{source_dir}/{pdfSort[new]}',f'{source_dir}/{new}.{pdfSort[new]}')
    
    
    for item in os.listdir(source_dir):
        if item.endswith('pdf'):
            print(item)
            Mitem = os.path.join(source_dir,item)
            print(Mitem)
            merger.append(Mitem)
            
    merger.write(f'{source_dir}/Night Audit Report 011221.pdf')
    merger.close
    