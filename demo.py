from PyQt5 import QtCore, QtWidgets
import sys


class BillUpload(QtWidgets.QWidget):
    def __init__(self):
        super(BillUpload, self).__init__()
        self.width, self.height = 500, 300
        self.targ = ""
        self.resize(self.width, self.height)
        self.setWindowTitle("上传")

        # 文本
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(int(self.width * 0.4), int(self.height * 0.5), int(self.width * 0.2), 30))

        # 输入框
        self.input = QtWidgets.QLineEdit(self)
        self.input.setPlaceholderText("输入目录路径")
        self.input.setGeometry(QtCore.QRect(int(self.width*0.1), int(self.height*0.3), int(self.width*0.6), 30))
        # 上传按钮
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(int(self.width*0.75), int(self.height*0.3), int(self.width*0.2), 30))
        self.pushButton.setText("选择目录")
        self.pushButton.clicked.connect(self.sel_dir_click,no_receiver_check=True)

        # self.upload_action = QtWidgets.QAction("上传", self)
        # self.upload_action.triggered.connect(self.upload)
        # self.pushButton.addAction(self.sel_dir_click)

    # @QtCore.pyqtSlot()
    def sel_dir_click(self):
        self.targ = QtWidgets.QFileDialog.getExistingDirectory()
        # print(targ)
        self.label.setText('上传中请稍后...')
        self.input.setText(self.targ)
        self.upload()

    def upload(self):
        # fin_dir = os.path.join(self.targ, "已上传")
        # if not os.path.exists(fin_dir):
        #     pathlib.Path(fin_dir).mkdir(parents=True)

        # try:
        #     shutil.move(file_path, fin_dir)
        # except:
        #     shutil.copy(file_path, fin_dir)
        #     os.remove(file_path)
        #
        QtWidgets.QMessageBox.information(self, "提示", "上传完成！", QtWidgets.QMessageBox.Yes)
        # 文本
        self.label.setText("上传完成！")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = BillUpload()
    ui.show()
    sys.exit(app.exec_())
