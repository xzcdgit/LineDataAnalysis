from yaml import emit
import serialset
from PyQt5.QtCore import QThread, pyqtSignal
import time
class MyThread(QThread):
  '''
  多线程类 继承自qt多线程类 主要用于在gui运行的同时 
  循环和串口进行通信并实时发送回gui线程以更新界面数据
  '''
  data_signal = pyqtSignal(list) #串口获得的数据反馈给主线程的信号
  finish_signal = pyqtSignal(int) #线程结束信号
  def __init__(self,portname:str, baudrate:int, parent=None):
    '''
    构造函数
    @参数
    portname: 端口号
    baudrate: 波特率
    '''
    super(MyThread, self).__init__(parent)
    self.run_flag = True
    self.clear_flag = 0
    self.portname = portname
    self.baudrate = baudrate
  def threadFinish(self):
    '''
    线程结束 标识符设定 线程结束后会自动反馈信号 改变主线程的ui显示
    '''
    self.run_flag = False
  def clearflagSet(self,num:str):
    '''
    数据清零标识符设定
    '''
    self.clear_flag = num
  def run(self): 
    '''
    多线程 run方法重构
    '''
    try:
      self.serialopt = serialset.SerialCommunication() #创建串口类对象
      self.serialopt.serialCreate(self.portname,self.baudrate) #设置串口
    except Exception as e:
      self.finish_signal.emit(2)
      return
    while True:
      #st = time.time()
      data = self.serialopt.autoFresh()
      if(data!=0):
        self.data_signal.emit(data)
      if self.clear_flag !=0 :
        if self.clear_flag > 0:
          self.serialopt.clearData(self.clear_flag)
        else:
          for i in range(4):
            self.serialopt.clearData(i) 
        self.clear_flag = 0
      if self.run_flag == False:
        break
      time.sleep(0)
      #print(time.time()-st)
    self.serialopt.serialClose()
    self.finish_signal.emit(1)
