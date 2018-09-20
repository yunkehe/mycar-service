#!/usr/bin/python3
import pymysql
from model import config
db_config = config.db_config

def get_conn():
    conn = pymysql.connect(host=db_config.host,
                           user=db_config.user,
                           password=db_config.password,
                           database=db_config.database,
                           )

    return conn


def execute(conn, sql):
   cursor = conn.cursor()
   cursor.execute(sql)
   conn.commit()
   return cursor

def select(cursor, sql):
    cursor.execute(sql)
    return cursor


def insert(cursor, sql):
    cursor.execute(sql)


def update(cursor, sql):
    cursor.execute(sql)
