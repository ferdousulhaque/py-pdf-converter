# This is a sample Python script.
# Import the required Module
import tabula
import xlwt
from fastapi import FastAPI, File, UploadFile, Form
from starlette.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import Union
import uvicorn
import uuid


class Convert(BaseModel):
    file: UploadFile
    type: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.get("/")
async def main():
    content = """
<body>
<h3>PDF to CSV Converter</h3>
<form action="/pdf-converter?type=csv" enctype="multipart/form-data" method="post">
<input name="file" type="file" accept="application/pdf">
<input type="submit">
</form>
<h3>PDF to Excel Converter</h3>
<form action="/pdf-converter?type=xls" enctype="multipart/form-data" method="post">
<input name="file" type="file" accept="application/pdf">
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


@app.post("/pdf-converter")
async def converter(file: UploadFile, type: str):
    if type == 'csv':
        random_filename = str(uuid.uuid4()) + ".csv"
        tabula.convert_into(file.file, "output/" + random_filename, output_format="csv", pages='all')
        return FileResponse("output/" + random_filename, 200, None, None, None, file.filename + ".csv")
    elif type == 'xls':
        random_filename = str(uuid.uuid4()) + ".xls"
        df = tabula.read_pdf(file.file, pages='all')[0]
        df.head()
        df.to_excel("output/" + random_filename)
        return FileResponse("output/" + random_filename, 200, None, None, None, file.filename + ".xls")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
