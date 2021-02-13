import sys
import flow_tree_mv
import qtpy.QtWidgets as QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        view = flow_tree_mv.TreeView()
        model = flow_tree_mv.TreeModel()
        view.setModel(model)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(view)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    tool_panel = Window()
    tool_panel.show()
    sys.exit(app.exec_())
