from cgitb import text
from datetime import date
from operator import ge
import time
import json
# from xmlrpc.client import _DateTimeComparable
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

# List 0f json
json_obj = {
  "data": {
    "_id": "61dfb992fc3931f6ae65861d",
    "created_at": "2022-01-13 05:33:06.072785",
    "created_by": 26,
    "permissions": {
      "client": [{
        "grant": "false",
        "name": "view project charter",
        "perm": "view_project_charter"
      }, {
        "grant": "false",
        "name": "edit project charter",
        "perm": "edit_project_charter"
      }, {
        "grant": "false",
        "name": "add sections",
        "perm": "add_sections"
      }, {
        "grant": "false",
        "name": "edit sections",
        "perm": "edit_sections"
      }, {
        "grant": "false",
        "name": "add new rows",
        "perm": "add_new_rows"
      }, {
        "grant": "false",
        "name": "edit rows",
        "perm": "edit_rows"
      }, {
        "grant": "false",
        "name": "edit cloumns rows",
        "perm": "edit_cloumns_rows"
      }],
      "vendor": [{
        "grant": "false",
        "name": "edit project charter",
        "perm": "edit_project_charter"
      }, {
        "grant": "false",
        "name": "view project charter",
        "perm": "view_project_charter"
      }, {
        "grant": "false",
        "name": "add sections",
        "perm": "add_sections"
      }, {
        "grant": "false",
        "name": "edit sections",
        "perm": "edit_sections"
      }, {
        "grant": "false",
        "name": "add new rows",
        "perm": "add_new_rows"
      }, {
        "grant": "false",
        "name": "edit rows",
        "perm": "edit_rows"
      }]
    },
    "project": {
      "id": 86,
      "project_name": "Reverted Code"
    },
    "template": {
      "_id": "61d2f6efb55d874cc905c72f",
      "charter_id": "61d2f6efb55d874cc905c72f",
      "chatterData": 
      [
        {
        "headerIds": ["0f7e813f-4c0e-4441-b3a8-f73fc6a404b8", "ce27a278-48be-43a6-a50f-87492b252484", "ebfd3a46-bd9c-490a-a176-d6ee8c96c5a7"],
        "permissionsMatrix": [],
        "sectionMatrix": [
          [{
            "type": "text",
            "value": "Tasks"
          }, {
            "type": "date",
            "value": "Due Date"
          }, {
            "type": "date",
            "value": "Start Date"
          }, {
            "type": "number",
            "value": "Budget"
          }],
          [{
            "type": "text",
            "value": "Phase1"
          }, {
            "type": "date",
            "value": "2022-01-06T18:30:00.000Z"
          }, {
            "type": "date"
          }, {
            "type": "number"
          }],
          [{
            "type": "text",
            "value": "Phase 2"
          }, {
            "type": "date",
            "value": "2022-01-12T18:30:00.000Z"
          }, {
            "type": "date"
          }, {
            "type": "number"
          }],
          [{
            "type": "text",
            "value": "Phase 3"
          }, {
            "type": "date",
            "value": "2022-01-11T18:30:00.000Z"
          }, {
            "type": "date",
            "value": "2022-01-17T18:30:00.000Z"
          }, {
            "type": "number",
            "value": "3223"
          }]
        ],
        "sectionName": "project secyion"
      }, {
        "headerIds": [],
        "permissionsMatrix": [],
        "sectionMatrix": [
          [{
            "type": "text",
            "value": "Tasks"
          }]
        ],
        "sectionName": "Test section"
      }],
      "created_at": "Mon, 03 Jan 2022 13:15:27 GMT",
      "created_by": 26,
      "slug": "Web-Development",
      "title": "Web Development",
      "type": "charter",
      "updated_at": "Wed, 12 Jan 2022 13:00:21 GMT",
      "updated_by": 26
    },
    "updated_at": "2022-01-13 05:33:06.072785",
    "updated_by": 26,
    "valid": "true"
  },
  "err": "",
  "message": "",
  "status": 1
}
json_list = json.dumps(json_obj)
json_dict = json.loads(json_list )

data = []
for col in json_dict:
  data.extend(json_dict)
# for row in col:
  # print(row)
  # data = []
project = json_dict["data"]["project"]
chatterDatas = json_dict["data"]["template"]["chatterData"]
for chatter in chatterDatas:
  # data = []
  # print(chatter)
  data.append(chatter)
data.append(Spacer(10, 20))
sectionMatrixs = chatter["sectionMatrix"][0]
for type in sectionMatrixs:
  data.extend(type)
  sectionName = chatter["sectionName"]
  data.append(sectionName)
  print(data)
  print("#######",sectionName)
  # colkey = ck["type"]
  # colvlu = cv["value"]
  # print('\n',colkey,'\n',colvlu)




# print (json_dict["data"]["project"]["project_name"])
# print (json_dict["data"]["template"])

fileName = 'pdfTable.pdf'
pdf = SimpleDocTemplate(
    fileName,
    pagesize=letter
) 
table = Table(data)
# add Style
style = TableStyle([
    ('BACKGROUND',(0,0),(3,0),colors.green),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALING',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME',(0,0),(-1,0),'Courier-Bold'),
    ('FONTSIZE',(0,0),(-1,0), 14),
    ('BOTTOMPADDING',(0,0),(-1,0),12),
    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
])
table.setStyle(style)    
    # 2) Alternate background color
rowNumb = len(json_dict)
for i in range(1, rowNumb):
    if i % 2 == 0:
        bc = colors.burlywood
    else:
        bc = colors.beige

    ts = TableStyle([
        ('BACKGROUND',(0,i),(-1,-1), bc)
    ])        
    table.setStyle(ts)

    # add borders
ts = TableStyle([
    ('BOX',(0,0),(-1,-1),2,colors.black),
    ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
    ('LINEABOVE',(0,2),(-1,2),2,colors.green),
    ('GRID',(0,1),(-1,-1),2,colors.black),
])    
table.setStyle(ts)
elems = []
elems.append(table)
pdf.build(elems)