from PyPDF2 import PdfReader
from verify_danfe_layout import verify_danfe
from pathlib import Path
from openpyxl import Workbook
import os
import sys
sys.dont_write_bytecode = True

ROOT_DIR = Path(__file__).parent 
FOLDER_DIR = ROOT_DIR / "notas"
FILE_DIR = ROOT_DIR / "notas/nf2.pdf"


def list_pdf(file_path):
    pdf_object = PdfReader(file_path)
    for i, page in enumerate(pdf_object.pages):
        text = page.extract_text()
        lines = text.split("\n")
        result = verify_danfe(lines)
        return result if result else None


def start(folder_path):
    folder_path = Path(folder_path)
    notas = []
    erros = 0
    for file in folder_path.glob('*.pdf'):
        result = list_pdf(file)
        if result:
            notas.append(result)
        else:
            erros += 1
    print(notas)
    return notas, erros



def create_sheet(notas, erros, caminho):
    wb = Workbook()
    ws = wb.active
    ws.title = "Notas"
    for line in notas:
        ws.append([line])
    ws.append([f"Erros: {erros}"])
    wb.save(caminho)

