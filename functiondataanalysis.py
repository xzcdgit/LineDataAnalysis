#from matplotlib import lines
#from numpy.lib.function_base import angle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import shutil
def txtSave(filepath:str,txtstring:str):
    '''
    保存txt文件
    @param
    filepath: 保存路径
    txtstring: 需要保存的字符串
    '''
    fw = open(filepath,'w')
    fw.write(txtstring) #字符串写入文件
    print(filepath)
    fw.close()
def readCsv(pathname:str):
    '''
    函数功能: 读取csv文件的内容
    pathname: csv文件的路径地址
    return: 以dataframe的格式返回csv文件的内容
    '''
    data = pd.read_csv(pathname)
    return data
def fileSave(ori_filepath:str, save_filepath:str):
    '''
    函数功能: 保存（复制）文件
    ori_filepath: 源文件路径地址
    save_filepath: 目标路径地址
    '''
    shutil.copy(ori_filepath,save_filepath)
def listTofile(data_list:list,pathname:str):
    '''
    函数功能: 将list数据保存为csv文件
    data_list: 需要保存的数据
    pathname: 文件保存路径
    '''
    datalist = transList(data_list)
    datalist.to_csv(pathname,index=False)
##########################################################################
def csvSave(pathname:str,data_list:list):
    '''
    函数功能: 将数据列保存为文件（专用特殊）
    data_list: 需要保存的数据
    pathname: 文件保存路径（文件夹路径）
    return: 完整的文件路径名
    '''
    crename = time.strftime("%Y%m%d", time.localtime()) #文件夹名（日期）
    mkDir(pathname+'\\'+crename)   #创建文件夹
    foldername = pathname+'\\'+crename        #完整文件夹路径名
    filename = fileName(foldername)                    #新文件名
    filepath = pathname+'\\'+crename+'\\'+filename #完整文件路径名
    datalist = transList(data_list) #数据转换
    datalist.to_csv(filepath,index=False) #保存数据
    return filepath
def transList(datalist:list)->pd.DataFrame:
    '''
    list列表转换为panda.DataFrame
    @param 
    datalist: 输入的list数据
    @return
    dataframe: 增加列名并返回dataframe格式的数据
    '''
    name=['Senser01','Senser02','Senser03','Senser04']
    datalist = pd.DataFrame(columns=name,data=datalist)
    return datalist
def mkDir(fullpath:str): 
    '''
    创建文件夹
    @param
    fullpath: 需要创建的文件夹地址
    ''' 
    import os
    path = fullpath
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
      # 如果不存在则创建目录
      # 创建目录操作函数
      os.makedirs(path) 
      return 1,fullpath
    else:
      # 如果目录存在则不创建，并提示目录已存在
      return 0,fullpath
def fileName(file_dir:str):
    '''
    文件重命名函数（如果已有同名文件则文件名+1）专用
    @参数
    file_dir: 文件夹路径
    ''' 
    for root, dirs, files in os.walk(file_dir): 
        pass
    i = 1
    savename = '1.csv'
    while True:
        samename_flag = False
        for j in files:
            if j == savename:
                i =i+1
                savename = str(i)+'.csv'
                samename_flag = True
                break
        if samename_flag == False:
            return savename
################################################数据处理（通用方法）【
def RotationCurveX(csv:pd.DataFrame,column_name:str):
    '''
    函数功能: 左右翻转函数 输入X轴曲线
    @param
    csv: 待处理数据
    column_name: 待处理数据列的列名
    @return
    csv_tmp: 处理后的输出
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp[column_name] = -csv_tmp[column_name]
    csv_tmp = csv_tmp.sort_values(by=column_name)  #根据角度值排序   需要赋值才会变动
    csv_tmp = csv_tmp.reset_index(drop=True)          #重置索引
    return csv_tmp
def RotationCurveY(csv:pd.DataFrame,column_name:str):
    '''
    函数功能: 上下翻转函数 输入Y轴曲线
    csv: 待处理数据
    column_name: 待处理数据列的列名
    return: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp[column_name] = -csv_tmp[column_name]
    #csv_tmp = csv_tmp.sort_values(by=column_name)  #根据角度值排序   需要赋值才会变动
    csv_tmp = csv_tmp.reset_index(drop=True)          #重置索引
    return csv_tmp
def AutoRotationCurveY(csv:pd.DataFrame,column_name:str):
    '''
    函数功能: y向正校正 根据顶点的位置自动上下翻转函数数据
    csv: 待处理数据
    column_name: 待处理数据列的列名
    return: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    maxx = csv_tmp[column_name].max()
    minn = csv_tmp[column_name].min()
    meann = csv_tmp[column_name].mean()
    if (maxx-meann) > (2*(meann-minn)):  #求出定点为最大值还是最小值
        pass
    else:
        csv_tmp[column_name] = -csv_tmp[column_name]
    csv_tmp = csv_tmp.reset_index(drop=True)          #重置索引
    return csv_tmp
def AutoRotationCurveX(csv:pd.DataFrame,column_name:str):
    '''
    函数功能: x向正校正 根据角度自动左右翻转函数数据
    @param
    csv: 待处理数据
    column_name: 待处理数据列的列名
    @return
    int: 是否翻转过标识符
    pd.dataframe: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    #maxx = csv_tmp[column_name].max()
    minn = csv_tmp[column_name].min()
    #meann = csv_tmp[column_name].mean()
    k = 0
    if minn<-500:  #如果角度小于0则翻转角度
        csv_tmp[column_name] = -csv_tmp[column_name]
        k = 1
    csv_tmp = csv_tmp.sort_values(by=column_name)  #根据角度值重新排序   需要赋值才会变动
    csv_tmp = csv_tmp.reset_index(drop=True) #重置索引
    return k,csv_tmp
def MulEx(csv:pd.DataFrame,angle_name:str,line_name:str)->tuple[int,int,int,int,float,int]:
    '''
    函数功能: 求出数据中的最大值 最小值 极值等信息
    @param
    csv: 待处理数据
    angle_name: 待处理数据列的角度列 列名
    line_name: 待处理数据列的高度列 列名
    @return
    maxx: 最大值
    maxx_angle: 最大值对应的角度信息
    minn: 最小值
    minn_angle: 最小值对应的角度信息
    meann: 均值
    maxdif: 最大值和最小值的差值
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp = csv_tmp.reset_index(drop=True)          #重置索引

    maxx = csv_tmp[line_name].max()
    maxx_index = csv_tmp[line_name].idxmax()
    maxx_angle = csv_tmp[angle_name][maxx_index] #求首个最大值角度值

    minn = csv_tmp[line_name].min()
    meann = csv_tmp[line_name].mean()
    minn_index = csv_tmp[line_name].idxmin()
    minn_angle = csv_tmp[angle_name][minn_index] #求首个最小值角度值
    maxdif = maxx-minn          #最大差值
    return maxx,maxx_angle,minn,minn_angle,meann,maxdif
def MulXY(csv:pd.DataFrame,column_name:str,value:float):
    '''
    函数功能: 将函数数据等比例放大
    @param
    csv: 待处理数据
    column_name: 待处理数据列的列名
    value: 放大倍率
    @return
    csv_tmp: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp[column_name] = csv_tmp[column_name]*value
    return csv_tmp
def MoveXY(csv:pd.DataFrame,column_name:str,value:float):
    '''
    函数功能: 将函数数据等差变化
    @param
    csv: 待处理数据
    column_name: 待处理数据列的列名
    value: 等差值
    @return
    csv_tmp: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp[column_name] = csv_tmp[column_name]+value
    return csv_tmp
def AreaInterception(csv:pd.DataFrame,column_name:str,start_value:int,end_value:int):
    '''
    函数功能: 数据截取
    @param
    csv: 待处理数据
    column_name: 待处理数据列的列名
    start_value: 截取起始位置
    end_value: 截取终点位置
    @return
    csv_tmp: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp = csv_tmp[(csv_tmp[column_name] >= start_value) & (csv_tmp[column_name] <= end_value)] #截取该区域的型线
    csv_tmp = csv_tmp.reset_index(drop=True)  #重置索引
    return csv_tmp
def FindSymmetry(csv:pd.DataFrame,angle_name:str,line_name:str,cycle_value:int=10000):
    '''
    函数功能: 查找输入输入的对称轴（2次拟合函数曲线 求对称轴）
    @param
    csv: 待处理数据（只能为切片后的单周期数据）
    column_name: 待处理数据列的列名
    start_value: 截取起始位置
    end_value: 截取终点位置
    @return
    csv_tmp: 处理后的数据
    z: 一个包含三个元素的列表 为将数据二次拟合后  x²  x  的系数 以及常数 c  的值
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp = csv_tmp.reset_index(drop=True) #重置索引
    maxx = csv_tmp[line_name].max()             #最大值得位置
    minn = csv_tmp[line_name].min()             #最小值得位置
    top_index = csv_tmp[line_name].idxmin()  #查找首个最大值的索引
    top0_angle = csv_tmp[angle_name][top_index] #求首个最大值得角度值
    csv_tmp.loc[(csv_tmp[angle_name]<top0_angle), angle_name] = csv_tmp[csv_tmp[angle_name]<top0_angle][angle_name]+cycle_value#拼合升程部分
    csv_tmp = csv_tmp.sort_values(by=angle_name)  #根据角度值排序
    csv_tmp = csv_tmp.reset_index(drop=True) #重置索引

    csv_tmp1 = csv_tmp[(csv_tmp[line_name] >= maxx-0.5*(maxx-minn))]  #截取大于最高点*0.9 的区域
    csv_tmp1 = csv_tmp1.sort_values(by=angle_name)  #根据角度值排序
    csv_tmp1 = csv_tmp1.reset_index(drop=True) #重置索引

    x = csv_tmp1[angle_name]
    y = csv_tmp1[line_name]
    z = np.polyfit(x,y,2)  #二项式简单拟合
    #p = np.poly1d(z)
    #yvals = p(x)
    x_sym = -z[1]/z[0]/2   #求得对称轴
    #plt.plot(x,yvals)
    #print(x_sym)
    return x_sym,z
def FindTop(csv:pd.DataFrame,angle_name:str,line_name:str):
    '''
    函数功能: 查找顶点位置 根据顶点（最大值）点的数量 求中间点来近似求取对称轴（精度低 已弃用）
    @param
    csv: 待处理数据（单周期）
    angle_name: 待处理数据列角度列的列名
    line_name: 待处理数据列高度列的列名
    @return
    csv_tmp: 处理后的数据
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp = csv_tmp.reset_index(drop=True) #重置索引
    maxx = csv_tmp[line_name].max()
    minn = csv_tmp[line_name].min()
    meann = csv_tmp[line_name].mean()
    if (maxx-meann) > (2*(meann-minn)):  #求出顶点为最大值还是最小值
        top_value = maxx
        low_value = minn
        top_index = csv_tmp[line_name].idxmax()  #查找首个最高点的索引
    else:
        top_value = minn
        low_value = maxx
        top_index = csv_tmp[line_name].idxmin()  #查找首个顶点的索引
    numm = (csv_tmp[line_name] == top_value).sum()  #求顶点值总个数
    top0_index = top_index   #根据最高点数量偏移求第一个顶点的索引
    top1_index = top_index+numm-1   #根据最高点数量偏移求最后一个顶点的索引
    top0_angle = csv_tmp[angle_name][top0_index] #求首个顶点角度值
    top1_angle = csv_tmp[angle_name][top1_index] #求最后一个顶点角度值
    top_angle = int(0.5*(top0_angle+top1_angle)+0.5) #求两点角度均值并四舍五入
    return top_angle,top_value,low_value
def DoubleData(csv:pd.DataFrame,angle_name:str,cycle_value:int):
    '''
    函数功能: 将单周期的数据复制两份 然后全部合并  得到一个 显示三个周期的曲线
    @param
    csv: 待处理数据（单周期）
    angle_name: 待处理数据列角度列的列名
    cycle_value: 数据周期 默认10000
    @return
    csv_tmp: 处理后的数据 即原始数据的三重拼合版本
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp2 = csv.copy(deep=True)
    csv_tmp3 = csv.copy(deep=True)
    csv_tmp2[angle_name] = csv_tmp[angle_name]+cycle_value
    csv_tmp3[angle_name] = csv_tmp[angle_name]+2*cycle_value
    csv_tmp = pd.concat([csv_tmp,csv_tmp2,csv_tmp3],axis=0,join='inner')
    csv_tmp = csv_tmp.sort_values(by=angle_name)  #根据角度值排序
    csv_tmp = csv_tmp.reset_index(drop=True) #重置索引
    return csv_tmp
def AnglePosition(csv:pd.DataFrame,x_name:str,y1_name:str,y1_value:int,y2_name:str,y2_value:int,hight:int=5000)->tuple[int,int]:
    '''
    函数功能: 根据 高度数据列1和高度数据列2的值 来确定唯一点（例如用来确定正时点的角度位置）
    @param
    csv: 待处理数据（单周期）
    angle_name: 待处理数据列角度列的列名
    y1_name: 数据列1
    y1_value: 特定点 y1数据列的高度值
    y2_name: 数据列2
    y2_value: 特定点 y2数据列的高度值
    hight: y1 和 y2 的截取范围

    @return
    x: 特定点的x坐标
    y: 特定点的y坐标
    '''
    #先尝试截取y1 y2小范围内的数据 如果重合区间内的数据量少于三个则扩大截取范围继续尝试
    lenth = 0
    range = 0
    while lenth<=3:
        csv_tmp = csv.copy(deep=True)  #每次循环应重置dataframe
        range = range+0.0015
        csv_tmp = AreaInterception(csv_tmp,y1_name,y1_value-range*hight,y1_value+range*hight)  #根据y1截取范围
        csv_tmp = AreaInterception(csv_tmp,y2_name,y2_value-range*hight,y2_value+range*hight)  #将y1截取后的结果根据y2再次截取
        lenth = len(csv_tmp)
        if range>0.1:
            break
    #将正时点附近截得的型线进行一次拟合获得交点坐标（正时点坐标）
    if lenth>=3:  #
        x = csv_tmp[x_name]
        y1 = csv_tmp[y1_name]
        y2 = csv_tmp[y2_name]
        z1 = np.polyfit(x,y1,1)  #一项式简单拟合
        z2 = np.polyfit(x,y2,1)  #一项式简单拟合
        x = (z2[1]-z1[1])/(z1[0]-z2[0])
        y = z1[0]*x+z1[1]
        return x,y
    else:
        return 0,0
################################################数据处理（通用）】
################################################功能函数（特殊）【
def DataVerification(csv:pd.DataFrame,angle_colname:str,inlet_colname:str,exhaustlet_colname:str,start_angle:int=3000,cycle_value:int=10000,tolerance:int=28):
    '''
    函数功能: 中间函数 用于校验测量数据的准确性（通过判定测量周期和理论周期的误差来确定数据的准确性 功能暂时不完整 只校验了进气形线的数据）
    参数:
    csv: 待处理数据（原始数据）
    angle_name: 角度数据列的列名
    inlet_colname: 进气数据列的列名
    exlet_colname: 排气数据列的列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    tolerance: 允许的周期误差值
    返回值: 
    int: 0 校验失败    1校验通过
    '''
    csv_tmp0 = csv.copy(deep=True)
    maxx_angle = csv_tmp0[angle_colname].max()
    #角度校验
    end_angle = start_angle+cycle_value
    if end_angle<=maxx_angle:
        x_symlist = []
        x_symmin = csv_tmp0[angle_colname].min()*0.9
        while end_angle<=maxx_angle:
            csv_tmp = AreaInterception(csv_tmp0,angle_colname,start_angle,end_angle) #截取一个独立周期
            x_sym,z = FindSymmetry(csv_tmp,angle_colname,inlet_colname)
            #print(x_sym)
            if x_sym>x_symmin:#如果对称轴距离起点角度足够则为有效对称轴
                x_symlist.append(x_sym)
            start_angle = end_angle
            end_angle = start_angle+cycle_value
        i = 0
        key = 1
        lenth = len(x_symlist)
        while i<(lenth-1):
            cycle_test = x_symlist[i+1]-x_symlist[i]  #将相邻波峰对称轴相减得到周期
            #print(cycle_test)
            if abs(cycle_test-cycle_value) > tolerance: #如果测试周期和标准周期的差值大于 允差（tolerance）则返回0
                key = 0
            i = i+1
        return key
    else:
        return 0
def DataPreprocessing(csv:pd.DataFrame,angle_colname:str,start_angle:int,cycle_value:int=10000):
    '''
    函数功能: 中间函数 用于预处理测量的原始数据
    参数:
    csv: 待处理数据（原始数据）
    angle_name: 角度数据列的列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    返回值: 
    csv_tmp: 返回的dataframe数据（经过截取 复制 拼接 合成的一个包含三个完整周期数据的数据列）
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp = AreaInterception(csv_tmp,angle_colname,start_angle,start_angle+cycle_value) #截取一个独立周期
    csv_tmp = DoubleData(csv_tmp,angle_colname,cycle_value)  #复制三个周期并拼接 保证至少有一个完整的波峰和波谷
    return csv_tmp
################################################
def TrueSym(csv:pd.DataFrame,angle_colname:str,line_colname:str,start_angle:int,cycle_value:int=10000):
    '''
    函数功能: 查找对称轴
    参数:
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 需要处理的数据列 列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    返回值:
    x_sym: 正时点的角度信息
    z: 一个包含三个元素的列表  表示 数据经过二次拟合后的 x²  x 的系数 以及 常数 c   的值
    '''
    csv_tmp0 = csv.copy(deep=True)
    start_angle = csv_tmp0[angle_colname].min() #计算预处理曲线角度最小值
    error_flag = 0
    while True:
        csv_tmp = csv_tmp0.copy(deep=True)
        csv_tmp = AreaInterception(csv_tmp,angle_colname,start_angle,start_angle+cycle_value) #截取一个独立周期
        x_sym,z = FindSymmetry(csv_tmp,angle_colname,line_colname) #查找该周期内的对称轴位置
        if x_sym > csv_tmp0[angle_colname].max()-cycle_value*0.1:  #如果对称轴离终点过近
            error_flag = 1
            print('数据异常')
            break
        elif x_sym < csv_tmp0[angle_colname].min()+cycle_value*0.1:  #如果对称轴离起点过近 就重新找下个周期内的对称轴
            start_angle = start_angle+0.8*cycle_value
        else:
            break
    return x_sym,z
def TrueSymImg(csv,angle_colname,line_colname,start_angle,cycle_value=10000):
    '''
    函数功能: 查找对称轴 作图用  （忘记了和函数 TrueSym 算法上有什么区别）
    参数:
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 需要处理的数据列 列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    返回值:
    x_sym: 正时点的角度信息
    z: 一个包含三个元素的列表  表示 数据经过二次拟合后的 x²  x 的系数 以及 常数 c   的值
    '''
    csv_tmp0 = csv.copy(deep=True)
    start_angle = csv_tmp0[angle_colname].min() #计算预处理曲线角度最小值
    csv_tmp = csv_tmp0.copy(deep=True)
    csv_tmp = AreaInterception(csv_tmp,angle_colname,start_angle,start_angle+cycle_value) #截取一个独立周期
    x_sym,z = FindSymmetry(csv_tmp,angle_colname,line_colname) #查找该周期内的对称轴位置
    return x_sym,z
####################################
#以下函数 所有传入dataframe均为预处理后的dataframe
def SpeAngle(csv,angle_colname,spline_colname,inlet_colname,exlet_colname,start_angle,cycle_value=10000,inlet_value=0,exlet_value=0):
    '''
    函数功能: 求出正时点位置信息  如果正时点的位置刚好同时处于 进气凸轮和排气凸轮的基圆部分 将导致该函数计算失败
    参数: 9
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    spline_name: 正时点夹角的参考轴线数据列名（如 RV80 正时点将显示在排气凸轮线上 因此 该参数 传入 排气凸轮数据列的列名）
    inlet_colname: 进气数据列的列名
    exlet_colname: 排气数据列的列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    inlet_value: 正时点位置的参考 进气凸轮高度
    exlet_value: 正时点位置的参考 排气凸轮高度
    返回值: 2
    angle_position: 正时点的位置（角度信息）
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp[inlet_colname] = csv_tmp[inlet_colname]-inlet_value
    csv_tmp[exlet_colname] = csv_tmp[exlet_colname]-exlet_value
    #csv_tmp = DataPreprocessing(csv_tmp,angle_colname,start_angle,cycle_value)#数据预处理 获得一个周期的三重拼接
    sp_sym,z = TrueSym(csv_tmp,angle_colname,spline_colname,start_angle,cycle_value)#获取指定型线对称轴信息  RV145正时点角度是和指定凸轮轴线的夹角
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sp_sym-cycle_value*0.5,sp_sym) #根据指定型线的对称轴位置截取特定区域
    #求正时点位置
    csv_tmp = csv_tmp.copy(deep=True)
    angle_position = AnglePosition(csv_tmp,angle_colname,inlet_colname,0,exlet_colname,0,5000)   #根据正时点对应的进指定型线值查找正时点角度 需要传入一个周期
    sp_angle = sp_sym-angle_position[0]
    #返回正时点角度
    return sp_angle
def SpeAngleImg(csv:pd.DataFrame,angle_colname:str,spline_colname:str,inlet_colname:str,exlet_colname:str,start_angle:int,cycle_value:int = 10000,inlet_value:int=0,exlet_value:int=0):
    '''
    函数功能: 求出正时点位置信息并截取相应区域（突出正时点的位置信息）
    参数: 9
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    spline_name: 正时点夹角的参考轴线数据列名（如 RV80 正时点将显示在排气凸轮线上 因此 该参数 传入 排气凸轮数据列的列名）
    inlet_colname: 进气数据列的列名
    exlet_colname: 排气数据列的列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    inlet_value: 正时点位置的参考 进气凸轮高度
    exlet_value: 正时点位置的参考 排气凸轮高度
    返回值: 2
    csv_tmp: 处理后的数据 以 正时点为数据中心
    angle_position: 正时点的位置（角度信息）
    '''
    csv_tmp = csv.copy(deep=True)
    csv_tmp[inlet_colname] = csv_tmp[inlet_colname]-inlet_value
    csv_tmp[exlet_colname] = csv_tmp[exlet_colname]-exlet_value

    sp_sym,z = TrueSym(csv_tmp,angle_colname,spline_colname,start_angle,cycle_value)#获取指定型线对称轴信息  RV145正时点角度是和指定凸轮轴线的夹角
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sp_sym-cycle_value*0.5,sp_sym) #根据指定型线的对称轴位置截取特定区域
    #求正时点位置
    csv_tmp = csv_tmp.copy(deep=True)
    angle_position = AnglePosition(csv_tmp,angle_colname,inlet_colname,0,exlet_colname,0,5000)   #根据正时点对应的进指定型线值查找正时点角度 需要传入一个周期
    #根据正时点位置 截取附近的图像区间
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sp_sym-cycle_value*0.5,sp_sym) #根据指定型线的对称轴位置截取特定区域
    if angle_position[0]>sp_sym:
        angle_start = sp_sym-0.02*cycle_value
        angle_end = angle_position[0]+0.02*cycle_value
    else:
        angle_start = angle_position[0]-0.02*cycle_value
        angle_end = sp_sym+0.02*cycle_value
    csv_tmp = csv.copy(deep=True)
    csv_tmp = AreaInterception(csv_tmp,angle_colname,angle_start,angle_end) #截取特定区域
    return csv_tmp,angle_position
def ImgSym(csv:pd.DataFrame,angle_colname:str,inlet_colname:str,exlet_colname:str,start_angle:int,cycle_value:int=10000)->tuple[tuple[int,int],tuple[int,int]]:
    '''
    函数功能: 求进排气凸轮对称轴的(x,y)坐标
    @参数: 
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    inlet_colname: 进气数据列的列名
    exlet_colname: 排气数据列的列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    @返回值: 
    [inlet_sym,y1]: 进气形线的角度对称轴角度和它的高度值
    [exlet_sym,y2]: 排气形线的角度对称轴角度和它的高度值
    '''
    csv_tmp = csv.copy(deep=True)
    inlet_sym,z1 = TrueSymImg(csv_tmp,angle_colname,inlet_colname,start_angle,cycle_value)#获取进气型线对称轴信息
    exlet_sym,z2 = TrueSymImg(csv_tmp,angle_colname,exlet_colname,start_angle,cycle_value)#获取排气型线对称轴信息
    y1 = z1[0]*inlet_sym*inlet_sym+z1[1]*inlet_sym+z1[2]  #求对称轴x值对应y1值
    y2 = z2[0]*exlet_sym*exlet_sym+z2[1]*exlet_sym+z2[2]  #求对称轴x值对应y2值
    return [inlet_sym,y1],[exlet_sym,y2]
def AngleDif(csv:pd.DataFrame,angle_colname:str,inlet_colname:str,exlet_colname:str,start_angle:int,cycle_value:int=10000)->int:
    '''
    函数功能: 求取进排气形线对称轴的角度差
    @参数: 
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    inlet_colname: 进气数据列的列名
    exlet_colname: 排气数据列的列名
    start_angle:起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    @返回值: 
    angle_dif: 进排气形线的角度差值
    '''
    csv_tmp = csv.copy(deep=True)
    inlet_sym,z = TrueSym(csv_tmp,angle_colname,inlet_colname,start_angle,cycle_value)#获取进气型线对称轴信息
    exlet_sym,z = TrueSym(csv_tmp,angle_colname,exlet_colname,start_angle,cycle_value)#获取排气型线对称轴信息
    angle_dif = inlet_sym-exlet_sym
    return angle_dif
def SymHeight(csv:pd.DataFrame,angle_colname:str,line_colname:str,start_angle:int,cycle_value:int=10000)->tuple[int,int,int,int]:
    '''
    函数功能: 求取进排气形线对称轴的角度差
    @参数: 
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 待处理数据列的列名
    start_angle: 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    @返回值: 
    range: 极差（形线的最大值和最小值的差值）
    sym_high: 凸轮对称轴线上两点的高度差
    high_point: 高点的角度值
    low_point: 低点的角度值
    '''
    csv_tmp = csv.copy(deep=True)

    sym,z = TrueSym(csv_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取指定型线对称轴信息
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sym,sym+cycle_value) #根据指定型线的对称轴位置截取特定区域

    #求最大的高度差
    high_point = csv_tmp[line_colname].max()  #高点
    low_point = csv_tmp[line_colname].min()   #低点
    range = high_point-low_point #极差

    #求沿轴线的高度差
    csv_tmp1 = csv_tmp.copy(deep=True)
    csv_tmp1 = AreaInterception(csv_tmp1,angle_colname,sym+cycle_value*(-0.02),sym+cycle_value*0.02)  #根据y1截取范围
    x = csv_tmp1[angle_colname]
    y1 = csv_tmp1[line_colname]
    z1 = np.polyfit(x,y1,2)  #二项式简单拟合
    #p = np.poly1d(z)
    #yvals = p(x)
    top_point = z1[0]*sym*sym+z1[1]*sym+z1[2]   #带入拟合的二次函数求得此角度的y值

    csv_tmp1 = csv_tmp.copy(deep=True)
    csv_tmp1 = AreaInterception(csv_tmp1,angle_colname,sym+cycle_value*0.49,sym+cycle_value*0.51)  #根据y2截取范围
    #plt.plot(csv_tmp1[angle_colname],csv_tmp1[line_colname])
    #plt.show()
    x = csv_tmp1[angle_colname]
    y2 = csv_tmp1[line_colname]
    z2 = np.polyfit(x,y2,1)  #一项式简单拟合
    back_point = z2[0]*(sym+0.5*cycle_value)+z2[1] #带入拟合的一次函数求得此角度的y值
    sym_high = top_point-back_point
    #返回极差 和轴线上的高度差
    return range,sym_high,high_point,low_point
def MulBaseRun(csv:pd.DataFrame,angle_colname:str,line_colname:str,start_angle:int,base_range:int,cycle_value:int=10000)->tuple[int,int,int,int]:
    '''
    函数功能: 求指定形线的基圆跳动值
    @参数: 
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 待处理数据列的列名
    start_angle: 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    base_range: 基圆的角度范围     （会自动以基圆对称轴为中心截取这个范围内的形线数据）
    cycle_value: 角度周期值
    @返回值: 
    range: 极差（形线的最大值和最小值的差值）
    sym_high: 凸轮对称轴线上两点的高度差
    high_point: 高点的角度值
    low_point: 低点的角度值
    '''
    csv_tmp = csv.copy(deep=True)
    sym,z = TrueSym(csv_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取指定型线对称轴信息
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sym+0.5*(cycle_value-base_range),sym+0.5*(cycle_value+base_range)) #根据指定型线的对称轴位置截取基圆区域
    high_point = csv_tmp[line_colname].max()  #高点
    low_point = csv_tmp[line_colname].min()   #低点
    mean = csv_tmp[line_colname].mean()  #均值
    max_dif = high_point-low_point  #求基圆部分最大极差
    return max_dif
def MulDecHeight(csv:pd.DataFrame,angle_colname:str,line_colname:str,start_angle:int,base_range:int,dec_range:int=2000,cycle_value:int=10000)->int:
    '''
    函数功能: 求指定形线的基圆跳动值
    @参数: 
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 待处理数据列的列名
    start_angle: 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    base_range: 基圆的角度范围     （会自动以基圆对称轴为中心截取这个范围内的形线数据）
    dec_rang: 减压高度测量的角度范围
    cycle_value: 角度周期值
    @返回值: 
    dec_hight: 减压高度
    '''
    csv_tmp = csv.copy(deep=True)
    sym,z = TrueSym(csv_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取指定型线对称轴信息
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sym+0.5*(cycle_value-base_range),sym+0.5*(cycle_value+base_range)) #根据指定型线的对称轴位置截取基圆区域
    high_point = csv_tmp[line_colname].max()  #高点
    low_point = csv_tmp[line_colname].min()   #低点
    mean = csv_tmp[line_colname].mean()  #均值
    max_dif = high_point-low_point  #求基圆部分最大极差

    csv_tmp2 = csv.copy(deep=True)
    csv_tmp2 = AreaInterception(csv_tmp2,angle_colname,sym+0.5*(cycle_value-base_range),sym+0.5*(cycle_value-dec_range)) #根据指定型线的对称轴位置截取非减压基圆左区域

    csv_tmp3 = csv.copy(deep=True)
    csv_tmp3 = AreaInterception(csv_tmp3,angle_colname,sym+0.5*(cycle_value+dec_range),sym+0.5*(cycle_value+base_range)) #根据指定型线的对称轴位置截取非减压基圆右区域

    csv_tmp4 = pd.concat([csv_tmp2,csv_tmp3],axis=0,join='inner')   #拼合截取的两个基圆非减压区域 求取基圆平均高度
    csv_tmp4 = csv_tmp4.sort_values(by=angle_colname)  #根据角度值排序
    csv_tmp4 = csv_tmp4.reset_index(drop=True) #重置索引

    mean4 = csv_tmp4[line_colname].mean()  #均值

    dec_height = high_point-mean4 #求取减压高度

    return dec_height
def MulLiftRun(csv_des:pd.DataFrame,csv,angle_colname:str,line_colname:str,start_angle:int,lift_range:int,cycle_value:int=10000)->tuple[int,pd.DataFrame,pd.DataFrame,list]:
    '''
    函数功能: 求指定形线的基圆跳动值
    @参数: 
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 待处理数据列的列名
    start_angle: 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    base_range: 基圆的角度范围     （会自动以基圆对称轴为中心截取这个范围内的形线数据）
    dec_rang: 减压高度测量的角度范围
    cycle_value: 角度周期值
    @返回值: 
    dif_max: 跳动值
    csv_des_tmp: 设计值csv文件 对照组
    csv_tmp: 测量值 csv数据
    dif_list: 差值列表
    '''
    csv_tmp = csv.copy(deep=True)
    csv_des_tmp = csv_des.copy(deep=True)

    sym_des,z_des = TrueSym(csv_des_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取设计型线对称轴信息
    if sym_des < csv_des_tmp[angle_colname].min()+0.5*lift_range:
        sym_des = sym_des+cycle_value
    csv_des_tmp = AreaInterception(csv_des_tmp,angle_colname,sym_des-0.5*lift_range,sym_des+0.5*lift_range) #根据指定型线的对称轴位置截取区域的升程区域

    sym,z_test = TrueSym(csv_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取指定型线对称轴信息
    if sym < csv_tmp[angle_colname].min()+0.5*lift_range:
        sym = sym+cycle_value
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sym-0.5*lift_range,sym+0.5*lift_range) #根据指定型线的对称轴位置截取区域的升程区域

    sym_dif = sym-sym_des
    csv_tmp[angle_colname] = csv_tmp[angle_colname]-sym_dif
    dif_alist = []
    dif_vlist = []
    for i in csv_tmp[angle_colname]:
        tmp_value = csv_tmp[csv_tmp[angle_colname]==i][line_colname]
        i = int(i+0.5)
        des_value = csv_des[csv_des[angle_colname]==i][line_colname]
        try:
            des_value = float(des_value)
            tmp_value = float(tmp_value)
            dif = tmp_value-des_value
            dif_alist.append(i)
            dif_vlist.append(dif)
        except:
            pass
    dif_max = max(dif_vlist[1:])
    dif_min = min(dif_vlist[1:])
    if dif_max>=0 and dif_min<=0:
        mov_y = -(dif_max+dif_min)*0.5
    else:
        mov_y = min(abs(dif_max),abs(dif_min))
        mov_y = mov_y+0.5*abs(dif_max-dif_min)
        if dif_min>0:
            mov_y = -mov_y
    csv_tmp[line_colname] = csv_tmp[line_colname]+mov_y
    dif_vlist= [i+mov_y for i in dif_vlist] 
    dif_list = [dif_alist,dif_vlist]
    dif_max = max(dif_vlist)
    dif_min = min(dif_vlist)
    return dif_max,csv_des_tmp,csv_tmp,dif_list
def ShapeLine(csv_des:pd.DataFrame,csv:pd.DataFrame,angle_colname:str,line_colname:str,start_angle:int,cycle_value:int=10000):
    '''
    函数功能: 根据对称轴所在位置 将图像处理成以对称轴为中心的一个周期图像
    @参数: 
    csv_des: 设计形线数据
    csv: 待处理数据（已经经过预处理的数据 经过 去除初始区间的数据 截取单个周期 复制再拼接 处理后的数据）
    angle_name: 角度数据列的列名
    line_colname: 待处理数据列的列名
    start_angle: 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    @返回值: 
    csv_des_tmp: 设计数据处理反馈
    csv_tmp: 测量数据处理反馈
    '''
    csv_tmp = csv.copy(deep=True)
    csv_des_tmp = csv_des.copy(deep=True)
    sym_des,z_des = TrueSym(csv_des_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取设计型线对称轴信息
    if sym_des < csv_des_tmp[angle_colname].min()+0.5*cycle_value:
        sym_des = sym_des+cycle_value

    sym,z_test = TrueSym(csv_tmp,angle_colname,line_colname,start_angle,cycle_value)#获取指定型线对称轴信息
    if sym < csv_tmp[angle_colname].min()+0.5*cycle_value:
        sym = sym+cycle_value
    csv_tmp = AreaInterception(csv_tmp,angle_colname,sym-0.5*cycle_value,sym+0.5*cycle_value) #根据指定型线的对称轴位置截取一个周期区域

    sym_dif = sym-sym_des
    csv_tmp[angle_colname] = csv_tmp[angle_colname]-sym_dif
    return csv_des_tmp,csv_tmp

def polarplot(data_ori:pd.DataFrame,des_ori:pd.DataFrame,base_height:float,design_chosed:int,angle_colname:str,inlet_colname:str,exhaustlet_colname:str,start_angle:int,cycle_value:int,angle_coefficient:float,line_coefficient:float,tolerance:float):
    '''
    函数功能: 传入所有所需的参数 一键分析 形线的各类参数信息
    @参数: 
    data_ori: 测量形线原始数据
    des_ori: 设计形线原始数据
    angle_colname: 角度数据列的列名
    inlet_colname: 进气形线列名
    exhaustlet_colname: 排气形线列名
    spline_colname: 正时点的计算 基准形线列名
    start_angle: 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置
    cycle_value: 角度周期值
    angle_coefficient: 角度的 脉冲数->度 的比例系数
    line_coefficient: 高度的 脉冲数->mm 的比例系数
    tolerance: 计算得到周期和理论周期的允差值（用于判断测量的数据是否有问题）
    @返回值: 
    str: 所有计算结果 列为字符串并返回
    '''
    #数据校验
    texttips = []
    #数据校验
    try:
      key = DataVerification(data_ori,angle_colname,inlet_colname,exhaustlet_colname,start_angle,cycle_value,tolerance)
      if key:
          texttips.append("数据校验通过\n")
      else:
          texttips.append("数据校验未通过\n")
    except Exception as e:
      texttips.append("数据校验失败，检查测量数据\n")
    try:
    #设计数据预处理
      des_tmp = des_ori.copy(deep=True)
      des_tmp = DataPreprocessing(des_tmp,angle_colname,0,cycle_value) #截取（start_angle----start_angle+cycle_value）制定一个周期范围内的型线进行分析  将其复制3份并拼接
    except Exception as e:
      texttips.append("设计数据预处理失败，检查设计数据\n")
    #原始数据预处理
    try:
      data_tmp = data_ori.copy(deep=True)
      data_tmp = DataPreprocessing(data_tmp,angle_colname,start_angle,cycle_value) #截取（start_angle----start_angle+cycle_value）制定一个周期范围内的型线进行分析  将其复制3份并拼接
    except Exception as e:
      texttips.append("测试数据预处理失败，检查测量数据\n")
    #数据分析（建立在预处理完成的前提下）
        #极坐标作图
    try:
        theta = data_tmp[angle_colname]*angle_coefficient/360*2*np.pi
        r = data_tmp[inlet_colname]*line_coefficient+base_height
        ax = plt.subplot(111,projection='polar')
        ax.plot(theta,r,linewidth=3,color='red')
        ax.grid(True)
        plt.show()
        texttips.append("极坐标作图成功")  
    except Exception as e:
        texttips.append("极坐标作图失败")  
    str_text = ''
    for i in texttips:
        str_text = str_text+i+'\n\n'
    return str_text

def autodeal(data_ori:pd.DataFrame,des_ori:pd.DataFrame,angle_colname:str,inlet_colname:str,exhaustlet_colname:str,spline_colname:str,start_angle:int,cycle_value:int,angle_coefficient:float,line_coefficient:float,tolerance:float,inlet_value:int,exlet_value:int,base_range:int,lift_range:int,dec_colname:str,dec_range:int)->str:
    '''
    函数功能 传入所有所需的参数 一键分析 形线的各类参数信息
    @param data_ori 测量形线原始数据
    @param des_ori 设计形线原始数据
    @param angle_colname 角度数据列的列名
    @param inlet_colname 进气形线列名
    @param exhaustlet_colname 排气形线列名
    @param spline_colname 正时点的计算 基准形线列名
    @param start_angle 起始角度值 求取凸轮对称轴角度值时 选取的计算范围的起始位置 计算用的是脉冲数量(pul)
    @param cycle_value 角度周期值 实际计算用的是脉冲数量(pul)
    @param angle_coefficient 角度的脉冲数->度的比例系数
    @param line_coefficient 高度的脉冲数->mm的比例系数
    @param tolerance 测量的周期和理论周期的允差（用于判断测量的数据是否有问题）计算用的是脉冲数量(pul)
    @param inlet_value 位于正时点位置时 进气形线的高度值 计算用的是脉冲数量(pul)
    @param exlet_value 位于正时点位置时 排气形线的高度值 计算用的是脉冲数量(pul)
    @param base_range 基圆的角度范围（用于计算基圆的跳动) 计算用的是脉冲数量(pul)
    @param lift_range 升程的角度范围（用于计算升程的跳动）计算用的是脉冲数量(pul)
    @param dec_colname 减压高度 基准形线列名
    @param dec_range 减压高度的角度范围 计算用的是脉冲数量(pul)
    @return str 将所有计算结果合成一份报告返回
    '''
    #数据校验
    texttips = []
    #数据校验
    try:
      key = DataVerification(data_ori,angle_colname,inlet_colname,exhaustlet_colname,start_angle,cycle_value,tolerance)
      if key:
          texttips.append("数据校验通过\n")
      else:
          texttips.append("数据校验未通过\n")
    except Exception as e:
      texttips.append("数据校验失败，检查测量数据\n")
    try:
    #设计数据预处理
      des_tmp = des_ori.copy(deep=True)
      des_tmp = DataPreprocessing(des_tmp,angle_colname,0,cycle_value) #截取（start_angle----start_angle+cycle_value）制定一个周期范围内的型线进行分析  将其复制3份并拼接
    except Exception as e:
      texttips.append("设计数据预处理失败，检查设计数据\n")
    #原始数据预处理
    try:
      data_tmp = data_ori.copy(deep=True)
      data_tmp = DataPreprocessing(data_tmp,angle_colname,start_angle,cycle_value) #截取（start_angle----start_angle+cycle_value）制定一个周期范围内的型线进行分析  将其复制3份并拼接
    except Exception as e:
      texttips.append("测试数据预处理失败，检查测量数据\n")
    #数据分析（建立在预处理完成的前提下）
    #求正时点角度（保证初值 进气高度=0 排气高度=0时为正时点的位置）
    try:
        sp_angle = SpeAngle(data_tmp,angle_colname,spline_colname,inlet_colname,exhaustlet_colname,start_angle,cycle_value,inlet_value,exlet_value)
        texttips.append("正时点角度："+str(round(sp_angle*angle_coefficient,2))+"°")
    except Exception as e:
        texttips.append("求正时点角度失败，检查测量数据\n")
    #求进排气角度差
    try:
        inex_angle = AngleDif(data_tmp,angle_colname,inlet_colname,exhaustlet_colname,start_angle,cycle_value)
        texttips.append("进排气角度差："+str(round(inex_angle*angle_coefficient,2))+"°")
    except Exception as e:
        texttips.append("求进排气角度差失败，检查测量数据\n")
    #求进气型线的高度差
    try:
        in_height = SymHeight(data_tmp,angle_colname,inlet_colname,start_angle,cycle_value)
        texttips.append("进气形线轴线高度差："+str(round(in_height[1]*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("求进气轴线高度差失败，检查测量数据\n")
    try:
        texttips.append("进气形线极差："+str(round(in_height[0]*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("求进气极差失败，检查测量数据\n")
    #求排气型线的高度差
    try:
        ex_height = SymHeight(data_tmp,angle_colname,exhaustlet_colname,start_angle,cycle_value)
        texttips.append("排气形线轴线高度差："+str(round(ex_height[1]*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算排气轴线高度差失败，检查测量数据\n")
    try:    
        texttips.append("排气形线极差"+str(round(ex_height[0]*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算排气极差失败，检查测量数据\n")
    #求进气型线的基圆跳动
    try:
        in_baserun = MulBaseRun(data_tmp,angle_colname,inlet_colname,start_angle,base_range,cycle_value)
        texttips.append("进气形线基圆跳动："+str(round(in_baserun*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算进气基圆跳动失败，检查测量数据\n")    
    #求排气型线的基圆跳动
    try:
        ex_baserun = MulBaseRun(data_tmp,angle_colname,exhaustlet_colname,start_angle,base_range,cycle_value)
        texttips.append("排气形线基圆跳动："+str(round(ex_baserun*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算排气基圆跳动失败，检查测量数据\n")    
    #求取减压高度(默认求排气高度)
    try:
        dec_height = MulDecHeight(data_tmp,angle_colname,dec_colname,start_angle,base_range,dec_range,cycle_value)
        texttips.append("减压高度："+str(round(dec_height*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算减压高度失败，检查测量数据\n")    
    #进气型线的升程跳动
    try:
        in_dif_max,in_des_lift_tmp,in_lift_tmp,in_dif_list = MulLiftRun(des_tmp,data_tmp,angle_colname,inlet_colname,start_angle,lift_range,cycle_value)
        texttips.append("进气形线升程跳动："+str(round(in_dif_max*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算进气升程跳动失败，检查测量数据\n")   
    #排气型线的升程跳动
    try:
        ex_dif_max,ex_des_lift_tmp,ex_lift_tmp,ex_dif_list = MulLiftRun(des_tmp,data_tmp,angle_colname,exhaustlet_colname,start_angle,lift_range,cycle_value)
        texttips.append("排气形线升程跳动："+str(round(ex_dif_max*line_coefficient,3))+"mm")
    except Exception as e:
        texttips.append("计算排气升程跳动失败，检查测量数据\n")      
    #结果显示至gui界面

    
    #绘图
    try:
        des_tmp,data_tmp = ShapeLine(des_tmp,data_tmp,angle_colname,inlet_colname,start_angle,cycle_value)
        desin_point,desex_point = ImgSym(des_tmp,angle_colname,inlet_colname,exhaustlet_colname,start_angle,cycle_value)
        plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
        plt.title('形线图')
        plt.ylabel('相对高度（mm）')
        plt.xlabel('相对角度（°）')
        plt.plot(des_tmp[angle_colname]*angle_coefficient,des_tmp[inlet_colname]*line_coefficient,"*-k",label="设计进气形线")
        plt.plot(des_tmp[angle_colname]*angle_coefficient,des_tmp[exhaustlet_colname]*line_coefficient,".-b",label="设计排气形线")
        plt.plot(data_tmp[angle_colname]*angle_coefficient,data_tmp[inlet_colname]*line_coefficient,"*-r",label="测量进气形线")
        plt.plot(data_tmp[angle_colname]*angle_coefficient,data_tmp[exhaustlet_colname]*line_coefficient,".-g",label="测量排气形线")
        
        #求对称轴位置
        in_point,ex_point = ImgSym(data_tmp,angle_colname,inlet_colname,exhaustlet_colname,start_angle,cycle_value)
        plt.vlines([desin_point[0]*angle_coefficient, desex_point[0]*angle_coefficient], -5, 7, linestyles='dashed', colors='black')
        plt.vlines([in_point[0]*angle_coefficient, ex_point[0]*angle_coefficient], -5, 7, linestyles='dashed', colors='red')
        plt.legend(loc='upper left')
        plt.grid(ls='--',linewidth=0.5)  # 生成网格
        ax= plt.gca()
        x_major_locator=plt.MultipleLocator(10)
        y_major_locator=plt.MultipleLocator(0.2)
        ax.xaxis.set_major_locator(x_major_locator)
        ax.yaxis.set_major_locator(y_major_locator)
        plt.show()
        texttips.append("作图成功") 
    except Exception as e:
        texttips.append("作图失败")
    str_text = ''
    for i in texttips:
        str_text = str_text+i+'\n\n'
    return str_text
