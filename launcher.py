import sys
import qtpy.QtWidgets as QtWidgets


# https://gist.github.com/mottosso/c853b6fd9fb963e6f3e7c7a4f53b649d
class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tool_panel = Window()
    tool_panel.show()
    sys.exit(app.exec_())
