from layout import Ui_Frame
from app_principal import start, create_sheet
import sys
from PySide6.QtWidgets import QApplication, QFrame, QFileDialog, QMessageBox

class Frame(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.folder_path = None
        self.notas = None
        self.erros = None
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.selecionar_pasta)
        self.ui.pushButton_2.clicked.connect(self.salvar_excel)
        self.ui.pushButton_3.clicked.connect(self.gerar)
        
    def selecionar_pasta(self):
        pasta = QFileDialog.getExistingDirectory(self, "Selecionar pasta")
        if pasta:
            self.folder_path = pasta
            self.ui.textEdit.setText(pasta)
            
    def salvar_excel(self):
        if not hasattr(self, "notas") or not self.notas:
            QMessageBox.warning(
            self,
            "Nenhuma nota encontrada",
            "Não existem notas para salvar."
            )
            return
        
        caminho, _ = QFileDialog.getSaveFileName(self,"Salvar arquivo Excel","","Arquivos Excel (*.xlsx)")
        if not caminho:
            return
        create_sheet(self.notas, self.erros, caminho)
    
    def gerar(self):
        if self.folder_path:
            notas, erros = start(self.folder_path)
            if not notas:
                print("entrou aqui")
                self.ui.label_2.setText("Nenhuma nota extraida")
                return
            self.ui.label_2.setText("Notas extraídas com sucesso")
            self.notas = notas if notas else None
            self.erros = erros if erros else None
            
            

if __name__ == "__main__":
    app_principal = QApplication(sys.argv)
    window = Frame()
    window.show()
    sys.exit(app_principal.exec())