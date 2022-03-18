import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
doc = SimpleDocTemplate("report.pdf",pagesize=letter,
                        rightMargin=72,leftMargin=72,
                        topMargin=72,bottomMargin=18)

                    

# https://code-maven.com/creating-pdf-files-using-python
# https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
Story=[]
logo = "home.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "tin foil hat"
formatted_time = time.ctime()
full_name = "Expand My Business"

            

address_parts = ["Udyog Vihar", "Gurugram, HR 50158"]

im = Image(logo, 2*inch, 2*inch)
Story.append(im)
styles=getSampleStyleSheet()

styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
ptext = '%s' % formatted_time

Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
# Create return address
ptext = '%s' % full_name
Story.append(Paragraph(ptext, styles["Normal"]))   

for part in address_parts:
    ptext = '%s' % part.strip()
    Story.append(Paragraph(ptext, styles["Normal"]))   
Story.append(Spacer(1, 12))
ptext = 'Dear %s:' % full_name.split()[0].strip()

Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
ptext = 'We would like to welcome you to our subscriber base for %s Magazine! \
        You will receive %s issues at the excellent introductory price of $%s. Please respond by\
        %s to start receiving your subscription and get the following free gift: %s.' % (magName, 
                                                                                                issueNum,
                                                                                                subPrice,
                                                                                                limitedDate,
                                                                                                freeGift)
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = 'Thank you very much and we look forward to serving you.'
Story.append(Paragraph(ptext, styles["Justify"]))
Story.append(Spacer(1, 12))
ptext = 'Sincerely,'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 48))
ptext = 'Uday Kumar'
Story.append(Paragraph(ptext, styles["Normal"]))
Story.append(Spacer(1, 12))
doc.build(Story)