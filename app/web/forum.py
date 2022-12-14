from cgi import test
from re import T
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app
import app.forum_sql as forum_sql

forum = Blueprint('forum', __name__, url_prefix='/')

# 포럼 게시판 목록
@forum.route('/forumList', methods=['POST','GET'])
def ForumList():
    
    resultList = forum_sql.ForumDao.selectListForum()

    return render_template('/web/forum/forumList.html', resultList=resultList)

# 포럼 게시판 상세
@forum.route('/forumDetail', methods=['POST','GET'])
def ForumDetail():
    
    seq = request.values.get("seq")
    # 상세정보 조회
    result = forum_sql.ForumDao.selectForum(seq)

    # 조회수 증가
    forum_sql.ForumDao.updateForumHitCnt(seq)

    return render_template('/web/forum/forumDetail.html', result=result)

# 포럼 게시판 등록 폼
@forum.route('/forumInsertForm', methods=['POST','GET'])
def ForumInsertForm():
    return render_template('/web/forum/forumInsertForm.html')

# 포럼 게시판 등록
@forum.route('/forumInsert', methods=['POST','GET'])
def ForumInsert():

    sj = request.values.get("sj")
    cnts = request.values.get("cnts")
    pwd = request.values.get("pwd")

    forum_sql.ForumDao.insertForum(sj, cnts, pwd)

    return redirect('/forumList')
    
# 포럼 게시판 수정폼
@forum.route('/forumUpdateForm', methods=['POST','GET'])
def ForumUpdateForm():

    seq = request.values.get("seq")
    result = forum_sql.ForumDao.selectForum(seq)

    return render_template('/web/forum/forumInsertForm.html', result=result)

# 포럼 게시판 수정
@forum.route('/forumUpdate', methods=['POST','GET'])
def forumUpdate():

    seq = request.values.get("seq")
    sj = request.values.get("sj")
    cnts = request.values.get("cnts")
    pwd = request.values.get("pwd")

    forum_sql.ForumDao.updateForum(seq, sj, cnts, pwd)

    return redirect('/forumDetail?seq='+seq)

# 포럼 게시판 수정
@forum.route('/forumDelete', methods=['POST','GET'])
def forumDelete():

    seq = request.values.get("seq")

    forum_sql.ForumDao.deleteForum(seq)

    return redirect('/forumList')