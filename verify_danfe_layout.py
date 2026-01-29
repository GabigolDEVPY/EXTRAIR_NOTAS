from validate_docbr import CNPJ
import re
cnpj = CNPJ()

def verify_danfe(nota):
    position = 0
    for line in range(len(nota)):
        if nota[position] == "CHAVE DE ACESSO" and len(nota[position+1]) == 54:
            return nota[position+1].replace(" ", '')
        elif len(nota[position]) == 54 or len(nota[position]) == 44:
            nota = nota[position].replace(" ", "")
            cnpj_nota = nota[6:20]
            if cnpj.validate(cnpj_nota):
                return nota
        elif "Chave de acesso" in nota[position] and len(nota[position]) > 20:
            print("entrou na terceira condição")
            nota = re.search(r'\d+', nota[position]).group()
            cnpj_nota = nota[6:20]
            if cnpj.validate(cnpj_nota):
                return nota
        position += 1    
    return None