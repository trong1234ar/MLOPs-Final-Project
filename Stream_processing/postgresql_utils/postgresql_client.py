import pandas as pd
import psycopg2
from sqlalchemy import create_engine
'''
Tái sử dụng được psycopg2.connect() và cursor.execute()
Thay vì gọi lặp lại ở nhiều nơi, define client gồm các hàm cần thiết 
Lấy cột bảng, chạy query từ file .sql, trả về pd dataframe
=> Cần là gọi
'''

class PostgresSQLClient:
      def __init__(self, database, user, password, host="127.0.0.1", port="5433"):
            self.database = database
            self.user = user 
            self.password = password
            self.host = host
            self.port = port
      def create_connection(self):
            # establish the connection
            conn = psycopg2.connect(
                  database=self.database,
                  user=self.user,
                  password=self.password,
                  host=self.host,
                  port=self.port
            )
            return conn
      def execute_query(self, query):
            # Creating a cursor object using the cursor() method
            conn = self.create_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            # print(f"Query has been executed successfully!")
            # commit the changes
            conn.commit()
            # Closing the connection
            conn.close()
      def get_columns(self, table_name):
            engine = create_engine(
            f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}"
        )
            conn = engine.connect()
            df = pd.read_sql(f"select * from {table_name}", conn)
            return df.columns