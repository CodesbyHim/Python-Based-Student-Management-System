## `utils.py`

import csv
import re
from openpyxl import Workbook

def is_valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def is_valid_age(age):
    return age.isdigit() and 1 <= int(age) <= 120

def export_to_excel(data, filename="students.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.append(["ID", "Name", "Email", "Age", "Gender", "Course"])

    for row in data:
        ws.append(row)

    wb.save(filename)
    return filename

def export_to_csv(data, filename="students.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Email", "Age", "Gender", "Course"])
        writer.writerows(data)
    return filename
