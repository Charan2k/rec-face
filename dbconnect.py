import mysql.connector

mydb = mysql.connector.connect(
  host="ai-attendance-devjam.c92vkw0v7cnn.ap-south-1.rds.amazonaws.com",
  user="admin",
  passwd="admin123",
  database="test1"
)

cursor = mydb.cursor()
file = open('database.sql')
sql = file.read()

for result in cursor.execute(sql, multi=True):
  if result.with_rows:
    print("Rows produced by statement '{}':".format(
      result.statement))
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(
      result.statement, result.rowcount))
