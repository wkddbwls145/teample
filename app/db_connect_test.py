import pymysql

con = pymysql.connect(
    host = '112.220.89.100'
    , port = 1976
    , user = 'common'
    , passwd = '1111'
    , db = 'teamproject'
    , charset = 'utf8'
)

cursors = con.cursor()
#sql = 'SELECT NOW() FROM DUAL'
sql = '''
        SELECT *
        FROM TB_FORUM
    '''
cursors.execute(sql)

# data fetch
data = cursors.fetchall()
#data = con.DataFrame(data=cursors.fetchall(), columns=['SJ', 'CNTS'])

con.close()

print(data)