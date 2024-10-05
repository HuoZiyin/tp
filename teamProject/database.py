import pymysql

# 连接到远程 MySQL 数据库
connection = pymysql.connect(
    host='localhost',       # 数据库主机，localhost 表示本地主机
    user='root',   # MySQL 用户名
    password='123456', # MySQL 用户密码
    database='ClydeRyde', # 要访问的数据库名称
    charset='utf8mb4',      # 使用 utf8mb4 字符集以支持更多字符
    cursorclass=pymysql.cursors.DictCursor  # 使用字典游标，返回字典格式数据
)

try:
    # 创建游标对象
    with connection.cursor() as cursor:
        # 执行SQL查询
        sql = "SELECT * FROM users"
        cursor.execute(sql)

        # 获取查询结果
        results = cursor.fetchall()
        for row in results:
            print(row)
finally:
    # 关闭数据库连接
    connection.close()
