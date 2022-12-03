import pymysql

class QuizDao:
    def __init__(self):
        pass
    
    def selectListQuiz():
        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT SEQ
                , QESTION
                , IMG_SRC
                , SCORE
                , DIFF
            FROM (
                SELECT SEQ
                    , QESTION
                    , IMG_SRC
                    , SCORE
                    , DIFF
                FROM TB_QUIZ
                WHERE DIFF = 'E'
                ORDER BY RAND()
                LIMIT 0, 5
            ) E
            UNION ALL
            SELECT SEQ
                , QESTION
                , IMG_SRC
                , SCORE
                , DIFF
            FROM (
                SELECT SEQ
                    , QESTION
                    , IMG_SRC
                    , SCORE
                    , DIFF
                FROM TB_QUIZ
                WHERE DIFF = 'M'
                ORDER BY RAND()
                LIMIT 0, 3
            ) M
            UNION ALL
            SELECT SEQ
                , QESTION
                , IMG_SRC
                , SCORE
                , DIFF
            FROM (
                SELECT SEQ
                    , QESTION
                    , IMG_SRC
                    , SCORE
                    , DIFF
                FROM TB_QUIZ
                WHERE DIFF = 'H'
                ORDER BY RAND()
                LIMIT 0, 2
            ) H
        """
        curs.execute(sql)

        rows = curs.fetchall()
        print(rows)
        
        for e in rows:
            ex_list = []

            temp = {'SEQ':e[0],'QESTION':e[1],'IMG_SRC':e[2],'SCORE':e[3],'DIFF':e[4]}

            sql = """
                SELECT QUIZ_SEQ, SEQ, EX_TEXT, CORR_YN
                FROM TB_QUIZ_EX
                WHERE QUIZ_SEQ = %s
                ORDER BY SEQ
            """
            curs.execute(sql, temp['SEQ'])

            exDataList = curs.fetchall()
            
            # 보기 목록
            for ex in exDataList:
                ex_temp = {'QUIZ_SEQ':ex[0],'SEQ':ex[1],'EX_TEXT':ex[2],'CORR_YN':ex[3]}
                ex_list.append(ex_temp)

            temp['EX_LIST'] = ex_list

            ret.append(temp)
        
        db.commit()
        db.close()
        return ret

    def selectListQuizResult(name, pwd):
        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT A.SEQ
                , DATE_FORMAT(A.REG_DATE, '%%Y.%%m.%%d') AS REG_YMD
                , CAST(IFNULL(B.CORR_SCORE, 0) AS SIGNED) AS CORR_SCORE /* 획득점수 */
                , CAST(IFNULL(B.TOT_SCORE, 0) AS SIGNED) AS TOT_SCORE /* 총점 */
                , TIME_FORMAT(SEC_TO_TIME(90), '%%i:%%s') AS TIME /* 풀이시간 */
            FROM TB_QUIZ_RESULT A
            LEFT OUTER JOIN (
                SELECT A.RESULT_SEQ
                    , SUM(CASE WHEN B.CORR_YN = 'Y' THEN C.SCORE ELSE 0 END) AS CORR_SCORE
                    , SUM(C.SCORE) AS TOT_SCORE
                FROM TB_QUIZ_RESULT_DETAIL A
                LEFT OUTER JOIN TB_QUIZ_EX B ON A.QUIZ_SEQ = B.QUIZ_SEQ AND A.ANSWER_SEQ = B.SEQ
                LEFT OUTER JOIN TB_QUIZ C ON B.QUIZ_SEQ = C.SEQ
                GROUP BY A.RESULT_SEQ
            ) B ON A.SEQ = B.RESULT_SEQ
            WHERE NAME = %s
            AND PASSWORD = %s
        """
        curs.execute(sql, (name, pwd))
        
        rows = curs.fetchall()

        print(rows)
        for e in rows:
            temp = {'SEQ':e[0],'REG_YMD':e[1],'CORR_SCORE':e[2],'TOT_SCORE':e[3],'TIME':e[4]}
            ret.append(temp)
        
        db.commit()
        db.close()
        return ret;

    def selectListQuizResultDetail(seq):
        ret = []
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            SELECT A.RESULT_SEQ
                , A.QUIZ_SEQ
                , A.ANSWER_SEQ
                , A.QUIZ_ORDR
                , B.QESTION
                , B.IMG_SRC
                , B.SCORE
                , B.DIFF
            FROM TB_QUIZ_RESULT_DETAIL A
            LEFT OUTER JOIN TB_QUIZ B ON A.QUIZ_SEQ = B.SEQ
            WHERE A.RESULT_SEQ = %s
            ORDER BY A.QUIZ_ORDR
        """
        curs.execute(sql, seq)
        
        rows = curs.fetchall()
        for e in rows:

            ex_list = []

            temp = {'RESULT_SEQ':e[0],'QUIZ_SEQ':e[1],'ANSWER_SEQ':e[2],'QUIZ_ORDR':e[3],'QESTION':e[4],'IMG_SRC':e[5],'SCORE':e[6],'DIFF':e[7]}

            sql = """
                SELECT QUIZ_SEQ, SEQ, EX_TEXT, CORR_YN
                FROM TB_QUIZ_EX
                WHERE QUIZ_SEQ = %s
                ORDER BY SEQ
            """
            curs.execute(sql, temp['QUIZ_SEQ'])

            exDataList = curs.fetchall()
            
            # 보기 목록
            for ex in exDataList:
                ex_temp = {'QUIZ_SEQ':ex[0],'SEQ':ex[1],'EX_TEXT':ex[2],'CORR_YN':ex[3]}
                ex_list.append(ex_temp)

            temp['EX_LIST'] = ex_list

            ret.append(temp)
        
        db.commit()
        db.close()
        return ret
    
    def insertQuizResult(name, pwd, time):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            INSERT INTO TB_QUIZ_RESULT (
                NAME
                , PASSWORD
                , TIMER
                , REG_DATE
            ) VALUES (
                %s
                , %s
                , %s
                , NOW()
            )
        """

        curs.execute(sql, (name, pwd, time))
        db.commit()
        db.close()

        return curs.lastrowid
        

    def insertQuizResultDetail(quizSeq, quizOrdr, answerSeq, resultSeq):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        
        sql = """
            INSERT INTO TB_QUIZ_RESULT_DETAIL (
                QUIZ_SEQ
                , QUIZ_ORDR
                , ANSWER_SEQ
                , RESULT_SEQ
                , REG_DATE
            ) VALUES (
                %s
                , %s
                , %s
                , %s
                , NOW()
            )
        """

        curs.execute(sql, (quizSeq, quizOrdr, answerSeq, resultSeq))
        db.commit()
        db.close()
    
    def selectUserInfo(seq):
        db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
        curs = db.cursor()
        print("seq = " +seq)
        sql = """
            SELECT NAME, PASSWORD
            FROM TB_QUIZ_RESULT
            WHERE SEQ  =  %s
        """

        curs.execute(sql, (seq))
        
        rows = curs.fetchall()

        print(rows)
        for i in rows:
            rows = i;
        
        db.commit()
        db.close()
        return rows;

    def selectQuizResult(seq, name, pwd):
            ret = []
            db = pymysql.connect(host='112.220.89.100', port=1976, db='teamproject', user='common', password='1111', charset='utf8')
            curs = db.cursor()
            
            sql = """
                SELECT A.SEQ
                    , DATE_FORMAT(A.REG_DATE, '%%Y.%%m.%%d') AS REG_YMD
                    , CAST(IFNULL(B.CORR_SCORE, 0) AS SIGNED) AS CORR_SCORE /* 획득점수 */
                    , CAST(IFNULL(B.TOT_SCORE, 0) AS SIGNED) AS TOT_SCORE /* 총점 */
                FROM TB_QUIZ_RESULT A
                LEFT OUTER JOIN (
                    SELECT A.RESULT_SEQ
                        , SUM(CASE WHEN B.CORR_YN = 'Y' THEN C.SCORE ELSE 0 END) AS CORR_SCORE
                        , SUM(C.SCORE) AS TOT_SCORE
                    FROM TB_QUIZ_RESULT_DETAIL A
                    LEFT OUTER JOIN TB_QUIZ_EX B ON A.QUIZ_SEQ = B.QUIZ_SEQ AND A.ANSWER_SEQ = B.SEQ
                    LEFT OUTER JOIN TB_QUIZ C ON B.QUIZ_SEQ = C.SEQ
                    GROUP BY A.RESULT_SEQ
                ) B ON A.SEQ = B.RESULT_SEQ
                WHERE NAME = %s
                AND PASSWORD = %s
                AND SEQ = %s
            """
            curs.execute(sql, (name, pwd,seq))
            
            rows = curs.fetchall()

            print(rows)
            for e in rows:
                temp = {'SEQ':e[0],'REG_YMD':e[1],'CORR_SCORE':e[2],'TOT_SCORE':e[3]}
            
            db.commit()
            db.close()
            return temp;


if __name__ == '__main__':
    resultList = QuizDao().selectListQuiz('');
    print(resultList)