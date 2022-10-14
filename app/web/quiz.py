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

    level_ty = request.values.get("level_ty")

    resultList = quiz_sql.QuizDao.selectListQuiz(level_ty)

    return render_template('/web/quiz/quizForm.html', resultList=resultList)

# 테스트 메뉴 문제풀기 결과 등록
@quiz.route('/quizInsert', methods=['POST','GET'])
def QuizeInsert():

    # sj = request.values.get("sj")
    # cnts = request.values.get("cnts")
    # pwd = request.values.get("pwd")

    # quiz_sql.QuizDao.insertQuizResult()
    # quiz_sql.QuizDao.insertQuizResultDetail()

    return redirect('/web/quiz/quizResultList.html')

# 테스트 메뉴 결과 목록
@quiz.route('/quizResultList', methods=['POST','GET'])
def QuizResultList():

    name = request.values.get("name")
    pwd = request.values.get("pwd")

    resultList = quiz_sql.QuizDao.selectListQuizResult(name, pwd)

    return render_template('/web/quiz/quizResultList.html', resultList=resultList)

# 테스트 메뉴 결과 상세
@quiz.route('/quizResultDetail', methods=['POST','GET'])
def QuizResultDetail():

    seq = request.values.get("seq")

    resultList = quiz_sql.QuizDao.selectListQuizResultDetail(seq)

    return render_template('/web/quiz/quizResultDetail.html', resultList=resultList)