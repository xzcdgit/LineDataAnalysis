#专用配置文件读取写入文件
import configparser
class IniSetUp(object):
  '''
  配置文件操作类 用于读取或者写入配置文件的内容 内容固定 专用于相关程序
  '''
  def __init__(self,config_name:str):
    '''
    构造函数
    @参数
    config_name: ini配置文件的完整地址路径
    '''
    self.config_name = config_name #ini文件的地址
    self.configRead()#实例化时即执行读取ini文件参数内容
  def configRead(self):
    '''
    读取特定ini配置文件的内容
    '''
    config = configparser.RawConfigParser()
    config.read(self.config_name,encoding="utf-8")
    self.angle_colname = config["LineName"]["angle_colname"] #角度 列名
    self.inlet_colname = config["LineName"]["inlet_colname"] #进气凸轮 列名
    self.exhaustlet_colname = config["LineName"]["exhaustlet_colname"] #排气凸轮 列名
    self.dec_colname = config["LineName"]["dec_colname"] #减压高度 列名
    self.cycle_value = config["BuiltInParameters"]["cycle_value"]#测量周期值
    self.start_angle = config["BuiltInParameters"]["start_angle"]#有效数据起始
    self.tolerance = config["BuiltInParameters"]["tolerance"]#允差
    self.base_range = config["BuiltInParameters"]["base_range"]#基圆范围
    self.lift_range = config["BuiltInParameters"]["lift_range"]#升程范围
    self.dec_range = config["BuiltInParameters"]["dec_range"]#减压阀范围
    self.inlet_value = config["BuiltInParameters"]["inlet_value"]#处于正时点位置时的进气型线高度
    self.exlet_value = config["BuiltInParameters"]["exlet_value"]#处于正时点位置时的排气型线高度
    self.angle_coefficient = config["BuiltInParameters"]["angle_coefficient"]#角度系数（传感器周期脉冲数转角度）
    self.line_coefficient = config["BuiltInParameters"]["line_coefficient"]#长度系数（传感器单脉冲对应的实际长度）
  def configWrite(self): 
    '''
    将修改后的配置文件内容覆盖掉原来的内容
    原本不存在的内容将被新建
    '''
    config = configparser.RawConfigParser()
    config.add_section('Address')   #添加conf节点
    config.add_section('LineName')   #添加config节点

    config.set('LineName', 'angle_colname', self.angle_colname)   #添加值
    config.set('LineName', 'inlet_colname', self.inlet_colname)
    config.set('LineName', 'exhaustlet_colname', self.exhaustlet_colname)
    config.set('LineName', 'dec_colname', self.dec_colname)

    config.add_section('BuiltInParameters')   #添加config节点
    config.set('BuiltInParameters','cycle_value',self.cycle_value)
    config.set('BuiltInParameters','start_angle',self.start_angle)
    config.set('BuiltInParameters','tolerance',self.tolerance)
    config.set('BuiltInParameters','base_range',self.base_range)
    config.set('BuiltInParameters','lift_range',self.lift_range)
    config.set('BuiltInParameters','dec_range',self.dec_range)
    config.set('BuiltInParameters','inlet_value',self.inlet_value)
    config.set('BuiltInParameters','exlet_value',self.exlet_value)
    config.set('BuiltInParameters','angle_coefficient',self.angle_coefficient)
    config.set('BuiltInParameters','line_coefficient',self.line_coefficient)

    with open(self.config_name, 'w', encoding="utf-8") as fw:   #循环写入（with open 会在文件使用完毕后自动关闭文件）
      config.write(fw)