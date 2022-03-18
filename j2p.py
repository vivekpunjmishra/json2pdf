from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

fileName = 'pdfTable2.pdf'
pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter
) 


def genPinTable(pin):
    pinElemTable = None
# 1) Build Structure
    titleTable = Table([
        [pin.title]
    ], pinElemWidth)

    refNoTable = Table([
        ['Ref. No:', pin.refNo, 'N 100']
    ], [60, 120, 70])

    pinTable = Table([
        ['PIN:', pin.PIN]
    ], [60, 190])

    serialTable = Table([
        ['Serial No:', pin. serialNo]
    ],[60])

    #add Style
    dateTable = Table([
        [
            'Date:',
            pin.date.strftime('%m/%d/%Y'),
            pin.date.strftime('%I:%M:%S %p')
        ]
    ],[60])
    serialDateTable = Table([
        [serialTable],
        [dateTable]
    ])

    picture = Image(pin.picPath)
    picture.drawWidth = 30
    picture.drawWidth = 30
    picTable = Table([[picture]], 30, 30)

    serialDatePicTable = Table([
        [serialDateTable, picTable ]
    ],[190, 50])

    pinElemTable = Table([
        [titleTable],
        [refNoTable],
        [pinTable],
        [serialDatePicTable]
    ], pinElemWidth)

    # 2) Add Style

    return pinElemTable

pins = getPins()
p1 = genPinTable(pins[0])
p2 = genPinTable(pins[1])
p3 = genPinTable(pins[2])
p4 = genPinTable(pins[3])

mainTable = Table([
    [p1, p2],
    [p3, p4]
])

elems = []
# elems.append(table)
elems.append(mainTable)
pdf.build(elems)