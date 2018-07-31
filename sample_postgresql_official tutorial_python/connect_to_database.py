# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:07:43 2018

@author: aditya.shetty
"""

import psycopg2

if __name__ == '__main__':

    try:
        conn = psycopg2.connect(
            "dbname='sample' user='admin' host='localhost' password='123'")
    except Exception as e:
        print(e)

    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)

    cur.close()
    conn.close()
