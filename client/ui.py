import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')

        layout = QVBoxLayout()

        self.label_username = QLabel('Username:')
        layout.addWidget(self.label_username)

        self.input_username = QLineEdit(self)
        layout.addWidget(self.input_username)

        self.label_password = QLabel('Password:')
        layout.addWidget(self.label_password)

        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.input_password)

        self.button_login = QPushButton('Login', self)
        self.button_login.clicked.connect(self.handle_login)
        layout.addWidget(self.button_login)

        self.setLayout(layout)

    def handle_login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        if username == 'admin' and password == 'password':
            QMessageBox.information(self, 'Success', 'Login successful')
        else:
            QMessageBox.warning(self, 'Error', 'Bad username or password')


class Chat_Page(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Chat Page')

        layout = QVBoxLayout()

        self.label_chat = QLabel('Chat:')
        layout.addWidget(self.label_chat)

        self.input_chat = QLineEdit(self)
        layout.addWidget(self.input_chat)

        self.button_send = QPushButton('Send', self)
        self.button_send.clicked.connect(self.handle_send)
        layout.addWidget(self.button_send)

        self.setLayout(layout)

    def handle_send(self):
        chat = self.input_chat.text()
        print(chat)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Chat_Page()
    login.show()
    sys.exit(app.exec_())