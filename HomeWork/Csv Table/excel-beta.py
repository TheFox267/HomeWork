import sys
from PyQt5 import QtWidgets, uic
from tabulate import tabulate
import csv


def load_csv_file_func():
    """Upload csv file"""
    filename = QtWidgets.QFileDialog.getOpenFileName(main_window, 'Открыть таблицу', '', "Csv Files (*.csv)")[0]
    try:
        with open(filename, 'r') as csv_file:
            csv_table_func(csv_file)
    except:
        pass


def csv_table_func(file_object):
    """Downloading a table and displaying a table with data"""
    reader = csv.reader(file_object, delimiter=',')

    all_table = [line for line in reader]

    main_window.table.setHorizontalHeaderLabels(all_table[0])

    count_collumn = len(all_table[0])

    count_row = len(all_table) - 1

    main_window.table.setColumnCount(count_collumn)

    main_window.table.setRowCount(count_row)

    without_headers = all_table[1:]

    count = 0

    while count < count_row:
        for column in range(0, count_collumn, 1):
            main_window.table.setItem(count, column, QtWidgets.QTableWidgetItem(without_headers[count][column]))
        count += 1

    main_window.table.resizeColumnsToContents()


app = QtWidgets.QApplication(sys.argv)

main_window = uic.loadUi('MainWindow.ui')

main_window.load_button.clicked.connect(load_csv_file_func)

main_window.show()

app.exec_()
