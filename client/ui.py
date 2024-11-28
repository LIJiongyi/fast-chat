import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QListWidget, QTextEdit

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

        main_layout = QHBoxLayout()

        # 左侧按钮布局
        button_layout = QVBoxLayout()
        self.button_messages = QPushButton('消息列表', self)
        self.button_contacts = QPushButton('联系人', self)
        self.button_settings = QPushButton('设置', self)

        button_layout.addWidget(self.button_messages)
        button_layout.addWidget(self.button_contacts)
        button_layout.addWidget(self.button_settings)

        main_layout.addLayout(button_layout)

        # 中间消息列表
        self.message_list = QListWidget()
        main_layout.addWidget(self.message_list)

        # 右侧具体选中的消息框
        right_layout = QVBoxLayout()
        self.label_chat = QLabel('Chat:')
        right_layout.addWidget(self.label_chat)

        self.input_chat = QLineEdit(self)
        right_layout.addWidget(self.input_chat)

        self.button_send = QPushButton('Send', self)
        self.button_send.clicked.connect(self.handle_send)
        right_layout.addWidget(self.button_send)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        right_layout.addWidget(self.chat_display)

        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

    def handle_send(self):
        chat = self.input_chat.text()
        self.chat_display.append(chat)
        self.input_chat.clear()

# for test
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Chat_Page()
    login.show()
    sys.exit(app.exec_())