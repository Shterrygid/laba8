from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

app = QApplication([])
table = QTableWidget()
table.setWindowTitle("Учёт обуви")

# Установка количества строк и столбцов
table.setRowCount(3)
table.setColumnCount(2)

# Установка заголовков таблицы
table.setHorizontalHeaderLabels(["Бренд", "Количество"])

# Заполнение ячеек таблицы данными
table.setItem(0, 0, QTableWidgetItem("Adidas"))
table.setItem(0, 1, QTableWidgetItem("25"))
table.setItem(1, 0, QTableWidgetItem("Nike"))
table.setItem(1, 1, QTableWidgetItem("30"))
table.setItem(2, 0, QTableWidgetItem("Phuma"))
table.setItem(2, 1, QTableWidgetItem("40"))

# Отображение таблицы
table.show()
app.exec_()