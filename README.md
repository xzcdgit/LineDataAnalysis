# line_data_analysis #
形线数据采集和分析
## 主要功能
* 数据采集部分：和标准的modebus协议的485设备通讯 将多个设备的反馈信息整理成列表 保存至本地文件
* 数据分析部分：通过对数据的截取拼接再计算来拟合曲线并获得所需要的信息
## 注意事项
* 在记录数据时，不应该同时使用其他功能，可能会导致一些不在预期内的错误
* 在计算分析形线数据时会自动断开和串口的通讯连接
* inifiles 文件夹中存放的是软件的预设配置参数
## 已经发现但未修复的Bug
* 罕见 采集的数据中本该为0的数值变为了65535
