import pymysql

class ForumDao:
    def __init__(self):
        pass
    
    def selectListForum():
        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT SEQ
                , SJ
                , CNTS
                , HIT_CNT
                , DATE_FORMAT(REG_DATE, '%Y.%m.%d') AS REG_YMD
            FROM TB_FORUM
        """
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            temp = {'SEQ':e[0],'SJ':e[1],'CNTS':e[2],'HIT_CNT':e[3],'REG_YMD':e[4]}
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret

    def selectForum(seq):

        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT SEQ
                , SJ
                , CNTS
                , HIT_CNT
                , DATE_FORMAT(REG_DATE, '%%Y.%%m.%%d') AS REG_YMD
            FROM TB_FORUM
            WHERE SEQ = %s
        """
        curs.execute(sql, (seq))
        
        rows = curs.fetchall()
        for e in rows:
            temp = {'SEQ':e[0],'SJ':e[1],'CNTS':e[2],'HIT_CNT':e[3],'REG_YMD':e[4]}
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def insertForum(sj, cnts, pwd):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            INSERT INTO TB_FORUM (
                SJ
                , CNTS
                , PASSWORD
                , REG_DATE
            ) VALUES (
                %s
                , %s
                , %s
                , NOW()
            )
        """
        curs.execute(sql, (sj, cnts, pwd))
        db.commit()
        db.close()
    
    def updateForumHitCnt(seq):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()

        sql = """
            UPDATE TB_FORUM SET 
                HIT_CNT = HIT_CNT + 1
           WHERE SEQ = %s
        """
        curs.execute(sql, (seq))
        db.commit()
        db.close()

    def updateForum(seq, sj, cnts, pwd):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()

        sql = """
            UPDATE TB_FORUM SET 
                SJ = %s
                , CNTS = %s
                , MOD_DATE = NOW()
           WHERE SEQ = %s
             AND PASSWORD = %s 
        """
        curs.execute(sql, (seq, sj, cnts, pwd))
        db.commit()
        db.close()

    def delteteForum(seq):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = "DELETE FROM TB_FORUM WHERE SEQ = %s"
        curs.execute(sql, seq)
        db.commit()
        db.close()

if __name__ == '__main__':
    resultList = ForumDao().selectListForum();
    print(resultList)