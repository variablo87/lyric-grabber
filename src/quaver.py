from gui import main_window

import sys
from PyQt5 import QtCore, QtWidgets

class MainApp (QtWidgets.QApplication):
  def __init__(self, argv):
    super(MainApp, self).__init__(argv)

    self._window = main_window.MainWindow()
    self._window.show()
    self._window.setWindowTitle('Quaver')

  def event(self, event):
    if event.type() == QtCore.QEvent.FileOpen:
      self._window.generateFilepathList([event.url().toString().replace('file://', '')])
    elif event.type() == 20:
      sys.exit()
    else:
      pass
      # print('Type is {}'.format(str(event.type())))
    return True

def main():
  QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
  QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
  app = MainApp(sys.argv)
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()