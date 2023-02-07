# @Time : 2023/02/07 13:57
# @Author : xzc
# @Version : 10.3
import sys
from PyQt5.QtWidgets import QApplication
import maincontrol
#主函数入口
if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = maincontrol.MyMainWindow() #初始化窗口
  win.show()
  sys.exit(app.exec_())