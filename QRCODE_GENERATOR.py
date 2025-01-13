import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from QRCODE_UI import Ui_QRGENERATOR  # Import the generated UI class
import qrcode


class MainApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_QRGENERATOR()
        self.ui.setupUi(self)

        # Connect buttons to their respective actions
        self.ui.pushButton.clicked.connect(self.cancel_action)  # Cancel button
        self.ui.pushButton_2.clicked.connect(self.generate_qr)  # Generate button
        self.ui.pushButton_3.clicked.connect(self.open_github)  # Info button

    def cancel_action(self):
        """Closes the application."""
        self.close()

    def generate_qr(self):
        """Generates and saves a QR code."""
        url = self.ui.textEdit.toPlainText().strip()  # Get the URL
        file_name = self.ui.textEdit_2.toPlainText().strip()  # Get the file name

        if not url or not file_name:
            QMessageBox.warning(self, "Input Error", "Please enter both the URL and file name.")
            return

        try:
            qr = qrcode.QRCode(box_size=10, border=4)
            qr.add_data(url)
            image = qr.make_image(fill_color="black", back_color="white")
            image.save(file_name)

            QMessageBox.information(self, "Success", f"QR Code saved as: {file_name}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate QR Code.\nError: {str(e)}")

    def open_github(self):
        """Opens the GitHub profile in the default web browser."""
        github_url = "https://github.com/Jeyapranov?tab=repositories"
        webbrowser.open(github_url)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
