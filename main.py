import sys
import re

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit,
    QLabel,
    QFrame,
    QPushButton,
)
from PySide6.QtCore import Qt, QTimer


class AppBuilder(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App Builder")
        self.resize(1100, 700)

        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QHBoxLayout(main_widget)

        # =================================
        # LEFT SIDE - CODE EDITOR
        # =================================

        left_frame = QFrame()
        left_layout = QVBoxLayout(left_frame)

        heading = QLabel("💻 Code Editor")
        heading.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
            }
        """)

        left_layout.addWidget(heading)

        self.code_editor = QTextEdit()

        self.code_editor.setPlainText(
            'title = "My Business App"\n'
            'message = "Welcome!"'
        )

        left_layout.addWidget(self.code_editor)

        # =================================
        # RIGHT SIDE - MOBILE PREVIEW
        # =================================

        right_frame = QFrame()
        right_layout = QVBoxLayout(right_frame)

        preview_heading = QLabel("📱 Live Preview")

        preview_heading.setAlignment(Qt.AlignCenter)

        preview_heading.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
            }
        """)

        right_layout.addWidget(preview_heading)

        # Mobile phone
        self.mobile = QFrame()

        self.mobile.setFixedSize(330, 600)

        self.mobile.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 8px solid #222;
                border-radius: 35px;
            }
        """)

        mobile_layout = QVBoxLayout(self.mobile)

        # Title
        self.title_label = QLabel("My Business App")

        self.title_label.setAlignment(Qt.AlignCenter)

        self.title_label.setStyleSheet("""
            QLabel {
                font-size: 25px;
                font-weight: bold;
                color: #222;
                border: none;
            }
        """)

        # Message
        self.message_label = QLabel("Welcome!")

        self.message_label.setAlignment(Qt.AlignCenter)

        self.message_label.setStyleSheet("""
            QLabel {
                font-size: 20px;
                color: #555;
                border: none;
            }
        """)

        # Button
        self.button = QPushButton("Get Started")

        self.button.setStyleSheet("""
            QPushButton {
                background-color: #222;
                color: white;
                padding: 12px;
                border-radius: 10px;
                font-size: 16px;
                border: none;
            }
        """)

        mobile_layout.addStretch()
        mobile_layout.addWidget(self.title_label)
        mobile_layout.addSpacing(20)
        mobile_layout.addWidget(self.message_label)
        mobile_layout.addSpacing(30)
        mobile_layout.addWidget(self.button)
        mobile_layout.addStretch()

        right_layout.addWidget(
            self.mobile,
            alignment=Qt.AlignCenter
        )

        # =================================
        # ADD BOTH SIDES
        # =================================

        main_layout.addWidget(left_frame)
        main_layout.addWidget(right_frame)

        # =================================
        # LIVE UPDATE TIMER
        # =================================

        self.timer = QTimer()

        self.timer.timeout.connect(self.update_preview)

        self.timer.start(500)

    # =====================================
    # READ CODE AND UPDATE MOBILE
    # =====================================

    def update_preview(self):

        code = self.code_editor.toPlainText()

        title_match = re.search(
            r'title\s*=\s*["\'](.*?)["\']',
            code
        )

        message_match = re.search(
            r'message\s*=\s*["\'](.*?)["\']',
            code
        )

        if title_match:
            self.title_label.setText(
                title_match.group(1)
            )

        if message_match:
            self.message_label.setText(
                message_match.group(1)
            )


# =========================================
# START APP
# =========================================

app = QApplication(sys.argv)

window = AppBuilder()

window.show()

sys.exit(app.exec())