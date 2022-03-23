import sqlite3 as db
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from matplotlib.pyplot import MultipleLocator
import seaborn as sns


def readFronSqllite(db_path,exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory=db.Row     # 可访问列信息
    cursor.execute(exectCmd)    # 该例程执行一个 SQL 语句
    rows=cursor.fetchall()      # 该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    # return rows
    #print(rows[0][2]) # 选择某一列数据

    return [x[0] for x in rows] # 转为了list

# 解析ARPA 单帧信息
def readfromAppaFrame(ARPAFrame):
    subARPA=ARPAFrame.split(',')
    print(subARPA)

if __name__=="__main__":
    path = 'C://Users//420//Desktop//sss.db'
    time = readFronSqllite(path,"select time from Sensor1;")
    accelerateX = readFronSqllite(path,"select accelerateX from Sensor1;")
    accelerateY = readFronSqllite(path, "select accelerateY from Sensor1;")
    accelerateZ = readFronSqllite(path, "select accelerateZ from Sensor1;")
    angleX = readFronSqllite(path, "select angleX from Sensor1;")
    angleY = readFronSqllite(path, "select angleY from Sensor1;")
    angleZ = readFronSqllite(path, "select angleZ from Sensor1;")

    # 横坐标为时间处理'%Y-%m-%d %H:%M:%S'
    # print(time)
    # print(accelerateX)
    plt.plot(time,accelerateX)
    x_major_locator = MultipleLocator(5) # 设置x轴的坐标显示间隔
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)  # 设置x轴的坐标显示间隔
    plt.xticks(rotation=90,fontsize=3) # 坐标旋转，字体大小
    plt.show()



    # 单独绘图
    # plt.figure()
    # plt.title('angleZ')
    # plt.ylabel('sin(θ/2)')
    # plt.plot(angleZ)
    # plt.savefig("angleZ.png", dpi=300)

    # accelerate组合绘图
    # plt.figure(figsize=(20, 5))
    # plt.title('accelerate')
    # plt.ylabel('m/s2')
    # # x_major_locator = MultipleLocator(2)  # 设置x轴的坐标显示间隔
    # # ax = plt.gca()
    # # ax.xaxis.set_major_locator(x_major_locator)
    # plt.xticks(rotation=90) # 坐标旋转
    # plt.plot(time,accelerateX,color='green',linestyle='-')
    # plt.plot(time,accelerateY, color='blue', linestyle='-')
    # plt.plot(time,accelerateZ, color='red',linestyle='-')
    # plt.legend(["accelerateX", "accelerateY","accelerateZ"]) # 设置图例
    # plt.savefig("accelerate2222.png", dpi=300)

    # # angle组合绘图
    # plt.figure(figsize=(20, 5))
    # plt.title('angle')
    # plt.ylabel('rad/s')
    # plt.plot(angleX,color='green', label='angleX',linestyle='-')
    # plt.plot(angleY, color='blue', label='angleY', linestyle='-')
    # plt.plot(angleZ, color='red', label='angleZ', linestyle='-')
    # plt.legend(["angleX", "angleY", "angleZ"])
    # plt.savefig("angle.png", dpi=300)


