import openpyxl

from PART_C.DDT.write_excel import workbook


def get_login_data():
    workbook=openpyxl.load_workbook("C://Users//chaithraM//PycharmProjects//PythonProject//PART_C//DemoTrisentisFramework//tests//test_data//loginData1.xlsx")