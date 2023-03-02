# This is a sample Python script.
# Import the required Module
import tabula
import xlwt
from fastapi import FastAPI, File, UploadFile
from starlette.responses import HTMLResponse

app = FastAPI()

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

@app.get("/")
async def main():
    content = """
<body>
<form action="/pdf-converter/csv" enctype="multipart/form-data" method="post">
<input name="files" type="file" accept="application/pdf">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

@app.post("/pdf-converter/{type}")
def read_root(type: str, pdf_file: UploadFile):
    pdf_file.write(pdf_file.file.read())

    # contents = pdf_file.file.read()
    df = tabula.read_pdf("input/white.pdf", pages='all')[0]

    return {"filename": file.filename}

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.the
    # Read a PDF File
    df = tabula.read_pdf("input/white.pdf", pages='all')[0]
    # convert PDF into CSV
    #tabula.convert_into("white.pdf", "white.csv", output_format="csv", pages='all')
    #df.head()
    df.to_excel("output/white.xls")
    #print(df)
    #f = open("demofile2.xls", "a")
    #f.write(df)
    #f.close()


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')
