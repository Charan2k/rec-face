import mysql.connector

mydb = mysql.connector.connect(
  host="ai-attendance-devjam.c92vkw0v7cnn.ap-south-1.rds.amazonaws.com",
  user="admin",
  passwd="admin123"
)

cursor = mydb.cursor()
cursor.execute("create database test1")