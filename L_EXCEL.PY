import openpyxl
 
workbook = openpyxl.load_workbook('6thSem_topics.xlsx')
sheet = workbook.active
 
for row in sheet.iter_rows(values_only=True):
	print(row)