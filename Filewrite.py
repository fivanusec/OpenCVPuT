import csv
from datetime import date

class Writer:
    line_count = 0
    column_names = None
    def __init__(self):
        with open('attendance.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    self.line_count+=1
                    self.column_names= ", ".join(row)
                self.line_count+=1

    def show(self):
        with open('attendance.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    self.line_count+=1
                    self.column_names= ", ".join(row)
                print(f'\t{row[0]} was here on {row[1]}')
                self.line_count+=1

    def wirte(self, data):
        with open('attendance.csv', mode='a') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['\n'])
            writer.writerow([data,date.today()])