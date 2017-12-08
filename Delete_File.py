
import cx_Oracle
import sys

con = cx_Oracle.connect('admin/admin@localhost')
cur = con.cursor()
if(len(sys.argv) <= 3):

	if(len(sys.argv) == 3):
		if(sys.argv[2] == "-d"):
			sql = "SELECT GUID_DAGR FROM DAGR_FILE WHERE GUID_FILE = :1"
			cur.execute(sql, [sys.argv[1]])
			for result in cur:
				sql = "DELETE FROM DAGR WHERE GUID = :1"
				cur.execute(sql, [result[0]])
				sql = "DELETE FROM DAGR_DAGR WHERE GUID_1 = :1 or GUID_2 = :2"
				cur.execute(sql, [result[0]])

	sql = "DELETE FROM DAGR_FILE WHERE GUID_FILE = :1"
	cur.execute(sql, [sys.argv[1]])
	sql = "DELETE FROM FILES WHERE GUID = :1"
	cur.execute(sql, [sys.argv[1]])
	con.commit()
	cur.close()
	con.close()
