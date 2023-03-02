# This is a sample Python script.
# Import the required Module
import tabula
import xlwt

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.the
    # Read a PDF File
    df = tabula.read_pdf("white.pdf", pages='all')[0]
    # convert PDF into CSV
    #tabula.convert_into("white.pdf", "white.csv", output_format="csv", pages='all')
    #df.head()
    df.to_excel("white.xls")
    #print(df)
    #f = open("demofile2.xls", "a")
    #f.write(df)
    #f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
