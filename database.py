import mysql.connector
from mysql.connector import Error

try:
    # 连接到 MySQL 数据库
    connection = mysql.connector.connect(
        host='localhost',       # 数据库主机地址
        database='eVehicleSystem',  # 数据库名称
        user='root',   # 用户名
        password='123456'  # 密码
    )

    if connection.is_connected():
        print("成功连接到 MySQL 数据库")
        # 创建一个游标对象
        cursor = connection.cursor()
        sql = "1"
        # 执行一个
        while sql != "quit":
            sql = input()
            cursor.execute(sql)
            # record = cursor.fetchone()
            # print(f"你连接到的数据库是: {record}")
            try:
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except Error as e:
                print("no output")

            connection.commit()
            print("s")



except Error as e:
    print(f"连接数据库时出现错误: {e}")

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL 连接已关闭")
