import pymysql

class ForumDao:
    def __init__(self):
        pass
    
    def selectListForum():
        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT A.SEQ
                , A.SJ
                , A.CNTS
                , A.HIT_CNT
                , DATE_FORMAT(A.REG_DATE, '%Y.%m.%d') AS REG_YMD
                , (SELECT COUNT(*) FROM TB_FORUM_COMMENT WHERE A.SEQ = FORUM_SEQ) AS COMMENT_CNT
            FROM TB_FORUM A
            ORDER BY REG_DATE DESC
        """
        curs.execute(sql)
        
        rows = curs.fetchall()
        for e in rows:
            temp = {'SEQ':e[0],'SJ':e[1],'CNTS':e[2],'HIT_CNT':e[3],'REG_YMD':e[4],'COMMENT_CNT':e[5]}
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
                , NAME
                , PASSWORD
                , DATE_FORMAT(REG_DATE, '%%Y.%%m.%%d') AS REG_YMD
            FROM TB_FORUM
            WHERE SEQ = %s
        """
        curs.execute(sql, (seq))
        
        rows = curs.fetchall()
        for row in rows:
            data = {'SEQ':row[0],'SJ':row[1],'CNTS':row[2],'HIT_CNT':row[3],'NAME':row[4],'PASSWORD':row[5],'REG_YMD':row[6]}
            
        # for e in rows:
        #     temp = {'SEQ':e[0],'SJ':e[1],'CNTS':e[2],'HIT_CNT':e[3],'REG_YMD':e[4]}
        #     ret.append(temp)
        
        db.commit()
        db.close()
        return data
    
    def selectListForumComment(seq):
        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT FORUM_SEQ
                , SEQ
                , CNTS
                , DATE_FORMAT(REG_DATE, '%%Y.%%m.%%d') AS REG_YMD
            FROM TB_FORUM_COMMENT
            WHERE FORUM_SEQ = %s
            ORDER BY REG_DATE
        """
        curs.execute(sql, (seq))
        
        rows = curs.fetchall()
        print(rows)
        for e in rows:
            temp = {'FORUM_SEQ':e[0],'SEQ':e[1],'CNTS':e[2],'REG_YMD':e[3]}
            ret.append(temp)
            #print(temp)
        
        db.commit()
        db.close()
        return ret
    
    def insertForum(sj, cnts, name, pwd):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            INSERT INTO TB_FORUM (
                SJ
                , CNTS
                , NAME
                , PASSWORD
                , REG_DATE
            ) VALUES (
                %s
                , %s
                , %s
                , %s
                , NOW()
            )
        """
        curs.execute(sql, (sj, cnts, name, pwd))
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

    def updateForum(seq, sj, cnts, name, pwd):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()

        sql = """
            UPDATE TB_FORUM SET 
                SJ = %s
                , CNTS = %s
                , MOD_DATE = NOW()
           WHERE SEQ = %s
             AND NAME = %s
             AND PASSWORD = %s 
        """
        curs.execute(sql, (sj, cnts, seq, name, pwd))
        db.commit()
        db.close()

    def deleteForum(seq, name, pwd):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = "DELETE FROM TB_FORUM WHERE SEQ = %s AND NAME = %s AND PASSWORD = %s"
        curs.execute(sql, (seq, name, pwd))
        db.commit()
        db.close()

    def insertForumComment(seq, cnts):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            INSERT INTO TB_FORUM_COMMENT (
                FORUM_SEQ
                , SEQ
                , CNTS
                , REG_DATE
            ) VALUES (
                %s
                , (SELECT IFNULL(MAX(SEQ), 0) + 1 FROM TB_FORUM_COMMENT A WHERE FORUM_SEQ = %s)
                , %s
                , NOW()
            )
        """
        curs.execute(sql, (seq, seq, cnts))
        db.commit()
        db.close()

if __name__ == '__main__':
    resultList = ForumDao().selectListForum()
    print(resultList)