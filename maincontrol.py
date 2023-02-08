import os
import shutil
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
#matplot绘图库
import matplotlib.pyplot as plt
#自定义库
from maingui import Ui_MainWindow
import functiondataanalysis
import iniset
import threadset
import serialset
#ui界面设置类
class MyMainWindow(QMainWindow, Ui_MainWindow):

  def __init__(self, parent=None): 
    '''
    构造函数 主要是设置全局变量 关联信号和槽
    '''
    super(MyMainWindow, self).__init__(parent) #执行父类的构造函数
    self.setupUi(self) #继承窗口函数MyMainWindow.setupUi的所有变量 以便修改界面函数显示
    self.toolSet()#设置界面槽函数
    self.uivalueSet()#全局变量预设
    
  def uivalueSet(self): 
    '''
    全局变量设定
    '''
    try:
      self.record_data_list = [] #记录的数据保存列表
      self.record_flag = False #是否进行记录
      self.record_data_num = 0 #已经记录的数据数量
      self.userright = 0 #用户权限初值设置
      self.trpd = '123456' #用户登录密码
      self.xcvalue = 0 #数据修改值x预设值
      self.yincvalue = 0 #数据修改值进气y预设值
      self.yexcvalue = 0 #数据修改值排气y预设值
      self.cwd = os.getcwd() #获取程序文件所在位置
      self.openfile = self.cwd #选择打开文件时弹窗的默认文件路径初始化
      #self.csv_save_path = '' #csv文件保存路径名预设
      #加载配置文件
      self.ini_address = self.cwd+r'\inifiles\BuiltInParameters.ini'
      self.inipar = iniset.IniSetUp(self.ini_address) #加载配置文件
      #凸轮轴型号判定
      if self.comboBox_3.currentIndex() == 0:
        self.des_address = self.cwd+r'\inifiles\RV145设计值.csv'
      elif self.comboBox_3.currentIndex() == 1:
        self.des_address = self.cwd+r'\inifiles\RV80S设计值.csv'
      self.save_address = self.cwd
      #数据列名读取
      self.angle_colname = self.inipar.angle_colname
      self.inlet_colname = self.inipar.inlet_colname
      self.exhaustlet_colname = self.inipar.exhaustlet_colname
      self.dec_colname = self.inipar.dec_colname

      self.cycle_value = int(self.inipar.cycle_value)
      self.start_angle = int(self.inipar.start_angle)
      self.tolerance = int(self.inipar.tolerance)
      self.base_range = int(self.inipar.base_range)
      self.lift_range = int(self.inipar.lift_range)
      self.dec_range = int(self.inipar.dec_range)
      self.inlet_value = int(self.inipar.inlet_value)
      self.exlet_value = int(self.inipar.exlet_value)
      self.angle_coefficient = float(self.inipar.angle_coefficient)
      self.line_coefficient = float(self.inipar.line_coefficient)
      self.statusBar.showMessage("预设置加载成功",5000)
    except Exception as e:
      self.statusBar.showMessage('预设置加载错误：'+str(e))

  def toolSet(self):
    '''
    gui界面的按键槽函数设置连接
    '''
    self.pushButton_5.clicked.connect(self.readIni)  #读取配置文件参数
    self.pushButton_6.clicked.connect(self.saveIni)  #保存配置文件参数
    self.pushButton_16.clicked.connect(self.exportResults)  #导出计算结果
    self.pushButton_17.clicked.connect(self.userLogin)  #用户登录按钮
    self.pushButton_18.clicked.connect(self.userLogout)  #用户注销按钮
    self.pushButton.clicked.connect(self.chooseDir)  #打开文件
    self.pushButton_20.clicked.connect(self.chooseDir2)  #打开文件2
    self.pushButton_8.clicked.connect(self.allAnalysis)  #一键分析
    self.comboBox_3.activated[str].connect(self.transDesad) #凸轮型号切换
    self.pushButton_2.clicked.connect(self.changeLine) #修改数据
    self.pushButton_3.clicked.connect(self.undoData) #撤销修改数据
    self.pushButton_4.clicked.connect(self.drawing) #单一作图
    self.pushButton_21.clicked.connect(self.specialPointimg)  #正时点图像绘制
    self.pushButton_31.clicked.connect(self.polardraw) #极坐标绘图
    self.pushButton_22.clicked.connect(self.sercomSet) #串口连接
    self.pushButton_7.clicked.connect(self.sersearch) #可用串口查询
    self.pushButton_23.clicked.connect(lambda:self.clearSet(1)) #数据输入口1清零
    self.pushButton_24.clicked.connect(lambda:self.clearSet(2)) #数据输入口2清零
    self.pushButton_25.clicked.connect(lambda:self.clearSet(3)) #数据输入口3清零
    self.pushButton_26.clicked.connect(lambda:self.clearSet(4)) #数据输入口4清零
    self.pushButton_29.clicked.connect(lambda:self.clearSet(-1)) #数据输入口全部清零
    self.pushButton_27.clicked.connect(self.recordOpt) #记录数据
    self.pushButton_28.clicked.connect(self.csvfileSave) #保存数据
    self.pushButton_30.clicked.connect(self.savefolderOpen) #打开文件夹
    self.pushButton_19.clicked.connect(self.recordRead) #读取最近保存的文件
    self.pushButton_15.clicked.connect(self.savechangeData) #保存修改结果至文件
    self.tabWidget.currentChanged.connect(self.closeLink)#页面切换时断开和usb端口的链接

  def threadsts(self,finish_way:int):
    '''
    串口通信线程 结束时将返回结束状态并自动调用一次该函数
    @param finish_way 1表示线程正常结束   2表示线程运行异常（创建串口通信对象失败 可能是连接的串口名错误）结束
    '''
    if finish_way == 1:
      self.statusBar.showMessage('成功关闭串口',5000)
      self.pushButton_22.setText('连接')
    else:
      self.statusBar.showMessage('串口连接失败',5000)
      self.pushButton_22.setText('连接')

  def sercomSet(self):
    '''
    连接串口 并创建串口的循环通信线程
    '''
    if self.pushButton_22.text() == '连接':
      self.serthread = threadset.MyThread(self.lineEdit_2.text(),int(self.lineEdit_16.text())) #创建线程类对象
      self.serthread.data_signal.connect(self.callBack) #连接信号
      self.serthread.finish_signal.connect(self.threadsts) #连接信号
      self.serthread.start() #启动线程
      self.statusBar.showMessage('打开串口成功',5000)
      self.pushButton_22.setText('断开')
    else:
      self.serthread.threadFinish()#线程退出标识符置位
      self.serthread.wait()#等待线程退出
  def closeLink(self,current_index:int)->None:
    '''
    当页面切换时 如果串口处于连接状态 关闭串口线程
    @param current_index 当前的页面序号
    '''
    if(self.pushButton_27.text() == '完成记录' and current_index != 0):
      reply = QMessageBox.question(self, '提示信息', '请完成记录后再进行其他操作,否则可能会出错', QMessageBox.Yes)
      return
    if current_index != 0:
      if self.pushButton_22.text() == '断开':
        self.serthread.threadFinish()#线程退出标识符置位
        self.serthread.wait()#等待线程退出
  def sersearch(self):
    '''
    用于查询可用的串口名称 查询结果为字符串的形式
    '''
    serial_str = serialset.serialsearch()
    self.textBrowser.setText(serial_str)

  def callBack(self,data:list):
    '''
    串口通信线程 每当串口通信线程内的数据获得更新时 
    将会发送信号调用该函数刷新gui界面
    @param data 一个由整数构成的list，长度为4
    '''
    data_del = data
    if self.checkBox_10.isChecked():
      data_del[0] = -data[0]
    if self.checkBox_11.isChecked():
      data_del[1] = -data[1]
    if self.checkBox_12.isChecked():
      data_del[2] = -data[2]
    if self.checkBox_13.isChecked():
      data_del[3] = -data[3]
    self.label_36.setText(str(data_del[0]))
    self.label_37.setText(str(data_del[1]))
    self.label_38.setText(str(data_del[2]))
    self.label_39.setText(str(data_del[3]))
    if self.record_flag == True:
      self.record_data_list.append(data_del)
      self.record_data_num += 1
      if self.record_data_num > 80000:
        self.statusBar.showMessage('记录数据量超过80000组,自动结束记录',5000)
        self.recordOpt()
        self.record_data_num = 0

  def recordOpt(self):
    '''
    数据记录槽函数
    根据按键文件 调用该函数后 改变 数据记录标识符 
    '''
    if self.pushButton_27.text() == '开始记录':
      self.pushButton_27.setText('完成记录')
      self.statusBar.showMessage('正在记录...',5000)
      self.record_data_list = []
      self.record_flag = True
    else:
      self.record_flag = False
      self.pushButton_27.setText('开始记录')
      self.statusBar.showMessage('完成记录',5000)
      self.csvfileSave()
  def savefolderOpen(self):
    '''
    测量数据界面的打开文件保存文件夹按钮
    '''
    try:
      if self.lineEdit_15.text() != '':
        folder_path = os.path.split(self.lineEdit_15.text())
        os.startfile(folder_path[0])
        self.statusBar.showMessage('打开保存目录',5000)
    except Exception as e:
      self.statusBar.showMessage('路径有误,打开文件夹失败',5000)

  def csvfileSave(self):
    '''
    保存csv文件
    '''
    # 保存确定框
    reply = QMessageBox.question(self, '保存', '确定保存？', QMessageBox.Yes | QMessageBox.No , QMessageBox.Yes)
    if reply == QMessageBox.Yes:
      csv_save_fullpath = functiondataanalysis.csvSave(self.lineEdit_17.text(),self.record_data_list)
      self.statusBar.showMessage('已保存在 '+csv_save_fullpath,5000)
      self.lineEdit_15.setText(csv_save_fullpath)
      self.label_42.setText(csv_save_fullpath)
    else:
      self.statusBar.showMessage('取消保存，在新的记录开始之前可以使用保存记录按钮保存本次数据 ',5000)

  def clearSet(self,index:int):
    '''
    将数据清零标识符置位 清零下位机的累计数据
    @param index 参数1-4分别为清零四个传感器的累计计量值，参数-1一次性清空所有传感器的累计计量值
    '''
    self.serthread.clearflagSet(index)
    self.statusBar.showMessage('数据已清零',5000)

  def transDesad(self):
    '''
    更改当前待分析凸轮轴的型号  以匹配正确的设计形线值 以及 会影响正时点的计算方式
    '''
    if self.comboBox_3.currentIndex() == 0:
      self.des_address = self.cwd+r'\inifiles\RV145设计值.csv'
    elif self.comboBox_3.currentIndex() == 1:
      self.des_address = self.cwd+r'\inifiles\RV80S设计值.csv'
  
  def userLogin(self): 
    '''
    更改用户的登录状态，会影响到软件某些功能的使用
    ''' 
    if self.userright == 0:
      inpd = self.lineEdit_18.text()
      if inpd == self.trpd:
        self.userright = 1
        self.lineEdit_18.setEnabled(False)
        self.statusBar.showMessage('登录成功',5000)
      else:
        self.userright = 0
        self.statusBar.showMessage('密码错误',5000)
    else:
      self.statusBar.showMessage('用户已登录',5000)
  
  def userLogout(self):
    '''
    注销用户的登录状态，会影响到软件某些功能的使用
    ''' 
    if self.userright:
      self.userright = 0
      self.lineEdit_18.setEnabled(True)
      self.lineEdit_18.setText('')
      self.statusBar.showMessage('已注销',5000)
    else:
      self.statusBar.showMessage('用户未登录',5000)
  
  def readIni(self): 
    '''
    读取配置文件的参数并显示在界面上，需要用户处于登录状态
    '''
    if self.userright:
      self.inipar.configRead()
      self.lineEdit_3.setText(self.inipar.cycle_value)
      self.lineEdit_7.setText(self.inipar.start_angle)
      self.lineEdit_8.setText(self.inipar.base_range)
      self.lineEdit_9.setText(self.inipar.lift_range)
      self.lineEdit_10.setText(self.inipar.dec_range)
      self.lineEdit_11.setText(self.inipar.inlet_value)
      self.lineEdit_12.setText(self.inipar.exlet_value)
      self.lineEdit_13.setText(self.inipar.angle_coefficient)
      self.lineEdit_14.setText(self.inipar.line_coefficient)
      self.lineEdit_4.setText(self.inipar.angle_colname)
      self.lineEdit_5.setText(self.inipar.inlet_colname)
      self.lineEdit_6.setText(self.inipar.exhaustlet_colname)
      self.lineEdit_19.setText(self.inipar.dec_colname)
    else:
      self.statusBar.showMessage('用户未登录',5000)
  
  def saveIni(self): 
    '''
    将修改后的参数信息写入配置文件中，需要用户处于登录状态
    '''
    if self.userright:#如果用户已经登陆
      reply = QMessageBox.question(self,'确认提示','确认保存？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if reply == QMessageBox.Yes:
        self.inipar.cycle_value = self.lineEdit_3.text()
        self.inipar.start_angle = self.lineEdit_7.text()
        self.inipar.base_range = self.lineEdit_8.text()
        self.inipar.lift_range = self.lineEdit_9.text()
        self.inipar.dec_range = self.lineEdit_10.text()
        self.inipar.inlet_value = self.lineEdit_11.text()
        self.inipar.exlet_value = self.lineEdit_12.text()
        self.inipar.angle_coefficient = self.lineEdit_13.text()
        self.inipar.line_coefficient = self.lineEdit_14.text()
        self.inipar.angle_colname = self.lineEdit_4.text()
        self.inipar.inlet_colname = self.lineEdit_5.text()
        self.inipar.exhaustlet_colname = self.lineEdit_6.text()
        self.inipar.dec_colname = self.lineEdit_19.text()
        self.inipar.configWrite()
        self.statusBar.showMessage('保存成功',5000)
      else :
        self.statusBar.showMessage('未保存',5000)
    else:
      self.statusBar.showMessage('用户未登录',5000)
  
  def chooseDir(self):
    '''
    打开本地磁盘上的形线数据文件，文件格式为csv
    '''
    file_choose = QFileDialog.getOpenFileName(self,'选择文件', self.openfile,'Excel files(*.csv);;All files(*)')
    if file_choose[0] != '':
      try:
        folder_path, file_name = os.path.split(file_choose[0])
        shutil.copy(file_choose[0],self.cwd+'\\tmp.csv')
        self.statusBar.showMessage('成功读取文件',5000)
        self.label_41.setText(file_choose[0])
        self.openfile = folder_path
      except Exception as e:
        self.statusBar.showMessage('文件打开错误'+str(e),5000)
    else:
      self.statusBar.showMessage('取消操作',5000)
  
  def recordRead(self):
    '''
    读取最近用数据记录功能记录的内存数据
    '''
    file_choose = self.label_42.text()
    if file_choose != '':
      try:
        folder_path, file_name = os.path.split(file_choose)
        shutil.copy(file_choose,self.cwd+'\\tmp.csv')
        self.statusBar.showMessage('成功读取最近文件',5000)
        self.label_41.setText(file_choose)
        self.openfile = folder_path
      except Exception as e:
        self.statusBar.showMessage('文件打开错误'+str(e),5000)
    else:
      self.statusBar.showMessage('空路径',5000)
  
  def chooseDir2(self):
    '''
    打开本地磁盘上的形线数据文件，文件格式为csv。
    区别于方式`chooseDir(self)`该方法读取的文件只可能在对比图像的绘制中被调用。
    '''
    file_choose = QFileDialog.getOpenFileName(self,'选择文件', self.openfile,'Excel files(*.csv);;All files(*)')
    if file_choose[0] != '':
      try:
        folder_path, file_name = os.path.split(file_choose[0])
        shutil.copy(file_choose[0],self.cwd+'\\tmp2.csv')
        self.statusBar.showMessage('打开文件成功',5000)
        self.textEdit_2.setText(file_choose[0])
        self.openfile = folder_path
      except Exception as e:
        self.statusBar.showMessage('文件打开错误'+str(e),5000)
    else:
      self.statusBar.showMessage('取消操作',5000)
  #修改文件数据（临时数据修改）
  def changeLine(self):
    '''
    修改形线数据，只是修改内存中的数据，未写入文件
    '''
    try:
      data_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
      self.xcvalue = self.xcvalue+self.doubleSpinBox.value()
      data_ori = functiondataanalysis.MoveXY(data_ori,self.angle_colname,int(self.doubleSpinBox.value()/self.angle_coefficient+0.5))
      if self.comboBox.currentIndex() == 0:
        self.yincvalue = self.yincvalue+self.doubleSpinBox_2.value()
        data_ori = functiondataanalysis.MoveXY(data_ori,self.inlet_colname,int(self.doubleSpinBox_2.value()/self.line_coefficient+0.5))
      elif self.comboBox.currentIndex() == 1:
        self.yexcvalue = self.yexcvalue+self.doubleSpinBox_2.value()
        data_ori = functiondataanalysis.MoveXY(data_ori,self.exhaustlet_colname,int(self.doubleSpinBox_2.value()/self.line_coefficient+0.5))
      functiondataanalysis.listTofile(data_ori,self.cwd+'\\tmp.csv')
      self.statusBar.showMessage('临时数据修改成功',5000)
    except Exception as e:
      self.statusBar.showMessage('数据修改失败',5000)

  #撤销所有的修改（针对临时数据）
  def undoData(self): 
    '''
    撤销对内存中数据的修改，未写入文件
    '''
    try:
      data_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
      data_ori = functiondataanalysis.MoveXY(data_ori,self.angle_colname,int(-self.xcvalue/self.angle_coefficient+0.5))
      data_ori = functiondataanalysis.MoveXY(data_ori,self.inlet_colname,int(-self.yincvalue/self.line_coefficient+0.5))
      data_ori = functiondataanalysis.MoveXY(data_ori,self.exhaustlet_colname,int(-self.yexcvalue/self.line_coefficient+0.5))
      functiondataanalysis.listTofile(data_ori,self.cwd+'\\tmp.csv')
      self.statusBar.showMessage('该形线所有修改已撤销',5000)
    except Exception as e:
      self.statusBar.showMessage('撤销失败'+str(e),5000)
  
  def savechangeData(self):
    try:
      file_choose = QFileDialog.getSaveFileName(self,'选择保存路径', self.openfile,'Excel files(*.csv)')
      if file_choose[0] != '':
          filepath = file_choose[0]                    
          functiondataanalysis.fileSave(self.cwd+'\\tmp.csv',filepath)
      else:
        self.statusBar.showMessage('取消操作',5000)
    except Exception as e:
      self.statusBar.showMessage('保存失败'+str(e),5000)

  #手动选择绘图
  def drawing(self): 
    try:
      #绘图
      plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
      plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
      plt.title('形线图')
      plt.ylabel('相对高度(mm)')
      plt.xlabel('相对角度(°)')
      if self.checkBox.isChecked():
        des_ori = functiondataanalysis.readCsv(self.des_address)
        plt.plot(des_ori[self.angle_colname]*self.angle_coefficient,des_ori[self.inlet_colname]*self.line_coefficient,"*-k",label="设计进气形线")
      if self.checkBox_2.isChecked():
        des_ori = functiondataanalysis.readCsv(self.des_address)
        plt.plot(des_ori[self.angle_colname]*self.angle_coefficient,des_ori[self.exhaustlet_colname]*self.line_coefficient,".-b",label="设计排气形线")
      if self.checkBox_3.isChecked():
        data1_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
        plt.plot(data1_ori[self.angle_colname]*self.angle_coefficient,data1_ori[self.inlet_colname]*self.line_coefficient,"*-r",label="测量进气形线1")
      if self.checkBox_4.isChecked():  
        data1_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
        plt.plot(data1_ori[self.angle_colname]*self.angle_coefficient,data1_ori[self.exhaustlet_colname]*self.line_coefficient,".-g",label="测量排气形线1")
      if self.checkBox_8.isChecked():
        data2_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp2.csv')
        plt.plot(data2_ori[self.angle_colname]*self.angle_coefficient,data2_ori[self.inlet_colname]*self.line_coefficient,"*-y",label="测量进气形线2")
      if self.checkBox_9.isChecked():  
        data2_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp2.csv')
        plt.plot(data2_ori[self.angle_colname]*self.angle_coefficient,data2_ori[self.exhaustlet_colname]*self.line_coefficient,".-c",label="测量排气形线2")
      plt.legend(loc='upper left')
      plt.grid(ls='--',linewidth=0.5)  # 生成网格
      ax= plt.gca()
      x_major_locator=plt.MultipleLocator(10)
      y_major_locator=plt.MultipleLocator(0.2)
      ax.xaxis.set_major_locator(x_major_locator)
      ax.yaxis.set_major_locator(y_major_locator)
      plt.show() #显示图像
      self.statusBar.showMessage('作图完成',5000)
    except Exception as e:
      self.statusBar.showMessage('作图错误'+str(e),5000)

  #独立功能 正时点图像 
  def specialPointimg(self): 
    texttips = ''
    des_ori = functiondataanalysis.readCsv(self.des_address)
    data_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
    #数据校验
    try:
      key = functiondataanalysis.DataVerification(data_ori,self.angle_colname,self.inlet_colname,self.exhaustlet_colname,self.start_angle,self.cycle_value,self.tolerance)
      if key:
          texttips = texttips+"数据校验通过\n"
      else:
          texttips = texttips+"数据校验未通过\n"
    except Exception as e:
      texttips = texttips+"数据错误，未能校验\n"
    try:
    #设计数据预处理
      des_tmp = des_ori.copy(deep=True)
      des_tmp = functiondataanalysis.DataPreprocessing(des_tmp,self.angle_colname,0,self.cycle_value) #截取（start_angle----start_angle+cycle_value）制定一个周期范围内的型线进行分析  将其复制3份并拼接
    except Exception as e:
      texttips = texttips+"错误，设计数据预处理失败，检查设计数据\n"
    #原始数据预处理
    try:
      data_tmp = data_ori.copy(deep=True)
      data_tmp = functiondataanalysis.DataPreprocessing(data_tmp,self.angle_colname,self.start_angle,self.cycle_value) #截取（start_angle----start_angle+cycle_value）制定一个周期范围内的型线进行分析  将其复制3份并拼接
    except Exception as e:
      texttips = texttips+"错误，测量数据预处理失败，检查测量数据\n"
    #数据分析（建立在预处理完成的前提下）

    #求正时点图像（保证初值 进气高度=0 排气高度=0时为正时点的位置）
    spline_colname = self.exhaustlet_colname
    if self.comboBox_3.currentIndex() == 0:  #根据凸轮轴型号切换正时点计算方式
      spline_colname = self.exhaustlet_colname #凸轮轴型号为0（RV145时） 正时点夹角是正时点位置和排气凸轮对称线的夹角
    elif self.comboBox_3.currentIndex() == 1:
      spline_colname = self.exhaustlet_colname #凸轮轴型号为0（RV170时） 正时点夹角是正时点位置和排气凸轮对称线的夹角
    csv_tmp,sp_position = functiondataanalysis.SpeAngleImg(data_tmp,self.angle_colname,spline_colname,self.inlet_colname,self.exhaustlet_colname,self.start_angle,self.cycle_value,self.inlet_value,self.exlet_value)
    #绘图
    try:
      plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
      plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
      plt.title('形线图')
      plt.ylabel('相对高度(mm)')
      plt.xlabel('相对角度(°)')
      plt.plot(csv_tmp[self.angle_colname]*self.angle_coefficient,csv_tmp[self.inlet_colname]*self.line_coefficient,"*-r",label="进气形线部分图像")
      plt.plot(csv_tmp[self.angle_colname]*self.angle_coefficient,csv_tmp[self.exhaustlet_colname]*self.line_coefficient,".-g",label="排气形线部分图像")
      in_point,ex_point = functiondataanalysis.ImgSym(data_tmp,self.angle_colname,self.inlet_colname,self.exhaustlet_colname,self.start_angle,self.cycle_value)
      #desin_point,desex_point = FunctionDataAnalysis.ImgSym(des_tmp,self.angle_colname,self.inlet_colname,self.exhaustlet_colname,self.start_angle,self.cycle_value)
      plt.plot(sp_position[0]*self.angle_coefficient, sp_position[1]*self.line_coefficient, color='r')
      plt.scatter(sp_position[0]*self.angle_coefficient, sp_position[1]*self.line_coefficient, color='b')
      plt.scatter(sp_position[0]*self.angle_coefficient, sp_position[1]*self.line_coefficient, color='w', marker='o', edgecolors='g', s=200)
      #print(sp_position[0]*self.angle_coefficient,sp_position[1]*self.line_coefficient)
      plt.annotate('正时点'+str(round(ex_point[0]*self.angle_coefficient-sp_position[0]*self.angle_coefficient,2))+'°', xy=(sp_position[0]*self.angle_coefficient, sp_position[1]*self.line_coefficient), xytext=(sp_position[0]*self.angle_coefficient+1, sp_position[1]*self.line_coefficient+0.05)) 
      plt.vlines([ex_point[0]*self.angle_coefficient], -1, 2.5, linestyles='dashed', colors='red')
      plt.legend(loc='upper left')
      plt.grid(ls='--',linewidth=0.5)  # 生成网格
      ax = plt.gca()
      x_major_locator=plt.MultipleLocator(10)
      y_major_locator=plt.MultipleLocator(0.2)
      ax.xaxis.set_major_locator(x_major_locator)
      ax.yaxis.set_major_locator(y_major_locator)
      plt.show()
    except Exception as e:
      self.statusBar.showMessage('作图错误'+str(e),5000)

  #极坐标绘图
  def polardraw(self): 
    des_ori = functiondataanalysis.readCsv(self.des_address)
    data_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
    base_high = self.doubleSpinBox_3.value()
    design_chosed = self.checkBox_6.isChecked()
    #根据凸轮轴型号选择正时点的夹角基准
    textstr = functiondataanalysis.polarplot(data_ori,des_ori,base_high,design_chosed,self.angle_colname,self.inlet_colname,self.exhaustlet_colname,self.start_angle,self.cycle_value,self.angle_coefficient,self.line_coefficient,self.tolerance)
    self.textEdit.setText(textstr)
  #导出计算结果
  def exportResults(self):
    reply = QMessageBox.question(self, '导出计算结果至地址栏填写的文件夹', '确认导出结果', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      functiondataanalysis.txtSave(self.label_42.text() + '.txt',self.textEdit.toPlainText())
      self.statusBar.showMessage('导出成功，导出至测量数据1所在文件夹',5000)

  #一键分析
  def allAnalysis(self): 
    '''
    一键自动分析形线的各种数据
    '''
    des_ori = functiondataanalysis.readCsv(self.des_address)
    data_ori = functiondataanalysis.readCsv(self.cwd+'\\tmp.csv')
    #根据凸轮轴型号选择正时点的夹角基准
    if self.comboBox_3.currentIndex() == 0:  #根据凸轮轴型号切换正时点计算方式  目前80和145均采用唯一点来计算正时点
      #145凸轮轴的 正时点计算基准线为排气凸轮对称轴位置
      spline_colname = self.exhaustlet_colname
    elif self.comboBox_3.currentIndex() == 1:  #根据凸轮轴型号切换正时点计算方式  目前80和145均采用唯一点来计算正时点
      #80凸轮轴
      spline_colname = self.exhaustlet_colname
    textstr = functiondataanalysis.autodeal(data_ori,des_ori,self.angle_colname,self.inlet_colname,self.exhaustlet_colname,spline_colname,self.start_angle,self.cycle_value,self.angle_coefficient,self.line_coefficient,self.tolerance,self.inlet_value,self.exlet_value,self.base_range,self.lift_range,self.dec_colname,self.dec_range)
    self.textEdit.setText(textstr)
  #导出计算结果
  def exportResults(self):
    reply = QMessageBox.question(self, '导出计算结果至地址栏填写的文件夹', '确认导出结果', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      functiondataanalysis.txtSave(self.label_41.text() + '.txt',self.textEdit.toPlainText())
      self.statusBar.showMessage('导出成功，导出至当前读取文件所在文件夹',5000)
  ##############################
  def closeEvent(self, event):
    '''
    重写qt事件中的退出事件，增加了退出的确认信息功能。pyqt事件的触发方法可以参考 [pyqt触发事件](https://blog.csdn.net/qq_42896653/article/details/100863417)
    @param event qt触发的退出事件
    '''
    reply = QMessageBox.question(self, '信息', '确认退出吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()
