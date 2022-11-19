from cgi import test
from re import T
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import app.quiz_sql as quiz_sql

quiz = Blueprint('quiz', __name__, url_prefix='/')

# 테스트 메뉴 첫화면
@quiz.route('/quizIntro', methods=['POST','GET'])
def QuizIntro():
    return render_template('/web/quiz/quizIntro.html')

# 테스트 메뉴 문제풀기
@quiz.route('/quizForm', methods=['POST','GET'])
def QuizForm():
    resultList = quiz_sql.QuizDao.selectListQuiz()

    return render_template('/web/quiz/quizForm.html', resultList=resultList)

# 테스트 메뉴 문제풀기 결과 등록
@quiz.route('/quizInsert', methods=['POST','GET'])
def QuizeInsert():

    print(request.values);
    name = request.values.get("name")
    pwd = request.values.get("pwd")

    quizSeqList = request.values.getlist("quiz_seq")
    answerSeqList = request.values.getlist("answer_seq")

    print("name = " + name)
    print("pwd = " + pwd)

    resultSeq = quiz_sql.QuizDao.insertQuizResult(name, pwd)

    for i in range(len(quizSeqList)) :
        quizSeq = quizSeqList[i]
        answerSeq = answerSeqList[i]
        quizOrdr = i + 1
        quiz_sql.QuizDao.insertQuizResultDetail(quizSeq, quizOrdr, answerSeq, resultSeq)


    resultList = quiz_sql.QuizDao.selectListQuizResult(name, pwd)
    return render_template('/web/quiz/quizResultList.html', resultList=resultList)

# 테스트 메뉴 결과 목록
@quiz.route('/quizResultList', methods=['POST','GET'])
def QuizResultList():

    print(request.values)
    name = request.values.get("name")
    pwd = request.values.get("pwd")

    resultList = quiz_sql.QuizDao.selectListQuizResult(name, pwd)

    return render_template('/web/quiz/quizResultList.html', resultList=resultList)

# 테스트 메뉴 결과 목록2
@quiz.route('/quizResultList2', methods=['POST','GET'])
def QuizResultList2():

    print(request.values)

    seq = request.values.get("seq")
    userInfo = quiz_sql.QuizDao.selectUserInfo(seq)

    resultList = quiz_sql.QuizDao.selectListQuizResult(userInfo[0], userInfo[1])

    return render_template('/web/quiz/quizResultList.html', resultList=resultList)

# 테스트 메뉴 결과 상세
@quiz.route('/quizResultDetail', methods=['POST','GET'])
def QuizResultDetail():

    print(request)
    print(request.values)
    seq = request.values.get("seq")
    print("seq = " + seq)

    #name = request.values.get("name")
    #pwd = request.values.get("pwd")
    userInfo = quiz_sql.QuizDao.selectUserInfo(seq)

    resultList2 = quiz_sql.QuizDao.selectQuizResult(seq, userInfo[0], userInfo[1])


    resultList = quiz_sql.QuizDao.selectListQuizResultDetail(seq)

    return render_template('/web/quiz/quizResultDetail.html', resultList=resultList, resultList2=resultList2)


#개발테스트 페이지 모음(따로빼야함)
@quiz.route('/quizIntro2', methods=['POST', 'GET'])
def quizIntro2():
    return render_template('/web/quiz/quizIntro2.html')

@quiz.route('/resultIntro', methods=['POST', 'GET'])
def resultIntro():
    return render_template('/web/quiz/resultIntro.html')

@quiz.route('/resultMain', methods=['POST', 'GET'])
def resultMain():
    return render_template('/web/quiz/resultMain.html')