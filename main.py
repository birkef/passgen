from generator import Generator

from PySide6.QtCore import (
    QSize as Size, Qt
)

from PySide6.QtWidgets import (
    QLabel as Label,
    QSpinBox as SpinBox,
    QCheckBox as CheckBox,
    QWidget as Widget,
    QMessageBox as MsgBox,
    QPushButton as Button,
    QGridLayout as GridL,
    QVBoxLayout as VBoxL,
    QHBoxLayout as HBoxL,
    QApplication as App,
    QMainWindow as MainWin,
    QLineEdit as LineEdit
)


class MainWindow(MainWin):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("birkPassgen")

        self.pwd = ""

        # Поле для сгенерированного пароля
        self.pwd_field = LineEdit()
        self.pwd_field.setPlaceholderText("Тут будет пароль")
        self.pwd_field.setAlignment(Qt.AlignCenter)
        self.pwd_field.textEdited.connect(self.__pwd_changed)

        # Длина пароля
        self.pwd_length_label = Label("Длина пароля:")

        self.pwd_length_spinbox = SpinBox()
        self.pwd_length_spinbox.setValue(16)
        self.pwd_length_spinbox.setRange(8, 24)
        self.pwd_length_spinbox.setStyleSheet("max-width: 65%;")

        self.pwd_length_symbols_label = Label("символов")

        self.pwd_length_layout = HBoxL()
        self.pwd_length_layout.addWidget(self.pwd_length_spinbox)
        self.pwd_length_layout.addWidget(self.pwd_length_symbols_label)

        # Переключение строчных букв
        self.lower_checkbox = CheckBox("Строчные буквы (a-z)")
        self.lower_checkbox.setChecked(True)

        # Переключение заглавных букв
        self.upper_checkbox = CheckBox("Заглавные буквы (A-Z)")
        self.upper_checkbox.setChecked(True)

        # Переключение цифр
        self.numbers_checkbox = CheckBox("Цифры (0-9)")
        self.numbers_checkbox.setChecked(True)

        # Переключение специальных символов
        self.specsyms_checkbox = CheckBox("Спец. символы")
        self.specsyms_checkbox.setChecked(True)

        # Кнопка "Сгенерировать"
        self.generate = Button("Сгенерировать")
        self.generate.clicked.connect(self.__generator)
        self.generate.setDefault(True)

        # Кнопка "По умолчанию"
        self.default = Button("По умолчанию")
        self.default.clicked.connect(self.__default)

        # Размещение элементов
        self.generator_layout = GridL()
        self.generator_layout.addWidget(self.pwd_length_label, 0, 0)
        self.generator_layout.addLayout(self.pwd_length_layout, 0, 1)
        self.generator_layout.addWidget(self.lower_checkbox, 1, 0)
        self.generator_layout.addWidget(self.upper_checkbox, 1, 1)
        self.generator_layout.addWidget(self.numbers_checkbox, 2, 0)
        self.generator_layout.addWidget(self.specsyms_checkbox, 2, 1)
        self.generator_layout.addWidget(self.default, 3, 0)
        self.generator_layout.addWidget(self.generate, 3, 1)

        self.main_layout = VBoxL()
        self.main_layout.addWidget(self.pwd_field, 0)
        self.main_layout.addLayout(self.generator_layout, 1)

        container = Widget()
        container.setLayout(self.main_layout)

        self.setFixedSize(Size(310, 150))

        self.setCentralWidget(container)

    def __generator(self):
        self.generate.setEnabled(False)
        self.default.setEnabled(False)

        generator = Generator(
            password_length=self.pwd_length_spinbox.value(),
            lower_registry=self.lower_checkbox.isChecked(),
            upper_registry=self.upper_checkbox.isChecked(),
            digits=self.numbers_checkbox.isChecked(),
            special_symbols=self.specsyms_checkbox.isChecked()
        )

        self.pwd = generator.new_password()

        try:
            self.pwd_field.setText(self.pwd)
        except ValueError:
            MsgBox.critical(
                self,
                "birkPassgen",
                "Вы не выбрали ни одного типа символов.\nВыберите хотя бы один тип символов и повторите попытку.\n"
            )

        self.generate.setEnabled(True)
        self.default.setEnabled(True)

    def __pwd_changed(self):
        if self.pwd_field.text() != self.pwd:
            self.pwd_field.setText(self.pwd)

    def __default(self):
        self.generate.setEnabled(False)
        self.default.setEnabled(False)

        self.pwd = ""
        self.pwd_field.setText(self.pwd)

        self.pwd_length_spinbox.setValue(16)
        self.lower_checkbox.setChecked(True)
        self.upper_checkbox.setChecked(True)
        self.numbers_checkbox.setChecked(True)
        self.specsyms_checkbox.setChecked(True)

        self.generate.setEnabled(True)
        self.default.setEnabled(True)


if __name__ == "__main__":
    app = App([])

    window = MainWindow()
    window.show()

    app.exec()
