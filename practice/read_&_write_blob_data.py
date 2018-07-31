"""

Created by ADITYA.SHETTY on 5/31/2018
 
"""

import psycopg2

if __name__ == '__main__':

    try:
        # conn = psycopg2.connect(
        # "dbname='sample' user='admin' host='localhost' password='$pass$456'")
        conn = psycopg2.connect(
            "dbname='sample' user='admin' host='localhost' password='$pass$456'")
    except Exception as e:
        print(e)

    cur = conn.cursor()

    '''
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    '''

    # write blob data (image) into database
    drawing = open(r'D:\Aditya\Aditya\source\spyder shorcuts.png', 'rb').read()
    cur.execute("INSERT INTO blob(file, test) " +
                "VALUES(%s,%s)",
                (psycopg2.Binary(drawing), 'img_1'))

    conn.commit()

    cur.execute('SELECT * FROM "blob"')
    records = cur.fetchall()
    # print(records)
    for r in records:
        print(r)

    # read blob data (image) from database
    cur.execute(""" SELECT file, test FROM blob WHERE test LIKE 'img_1';""")
    blob = cur.fetchone()
    open(r'C:\Users\aditya.shetty\Desktop\img.png', 'wb').write(blob[0])

    # deleting data from db
    '''
    cur.execute("DELETE from blob WHERE test LIKE %s;", ('adi',))
    rows_deleted = cur.rowcount
    print(rows_deleted)
    
    conn.commit()
    '''

    cur.close()
    conn.close()
