from cgi import test
from re import T
from flask import Blueprint, request, render_template, flash, redirect, url_for, jsonify
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

    commentList = forum_sql.ForumDao.selectListForumComment(seq)

    # 조회수 증가
    forum_sql.ForumDao.updateForumHitCnt(seq)

    return render_template('/web/forum/forumDetail.html', result=result, commentList=commentList)

# 포럼 게시판 등록 폼
@forum.route('/forumInsertForm', methods=['POST','GET'])
def ForumInsertForm():
    return render_template('/web/forum/forumInsertForm.html')

# 포럼 게시판 등록
@forum.route('/forumInsert', methods=['POST','GET'])
def ForumInsert():

    sj = request.values.get("sj")
    cnts = request.values.get("cnts")
    name = request.values.get("name")
    pwd = request.values.get("pwd")

    forum_sql.ForumDao.insertForum(sj, cnts, name, pwd)

    return redirect('/forumList')
    
# 포럼 게시판 수정폼
@forum.route('/forumUpdateForm', methods=['POST','GET'])
def ForumUpdateForm():

    seq = request.values.get("seq")
    name = request.values.get("name")
    pwd = request.values.get("pwd")

    result = forum_sql.ForumDao.selectForum(seq)

    return render_template('/web/forum/forumUpdateForm.html', result=result, name=name, pwd=pwd)

# 포럼 게시판 수정
@forum.route('/forumUpdate', methods=['POST','GET'])
def forumUpdate():

    seq = request.values.get("seq")
    sj = request.values.get("sj")
    cnts = request.values.get("cnts")
    name = request.values.get("name")
    pwd = request.values.get("pwd")

    print("seq = " + seq)
    print("sj = " + sj)
    print("cnts = " + cnts)
    print("name = " + name)
    print("pwd = " + pwd)

    forum_sql.ForumDao.updateForum(seq, sj, cnts, name, pwd)

    return redirect('/forumDetail?seq='+seq)

# 포럼 게시판 수정
@forum.route('/forumDelete', methods=['POST','GET'])
def forumDelete():

    seq = request.values.get("seq")
    name = request.values.get("name")
    pwd = request.values.get("pwd")

    forum_sql.ForumDao.deleteForum(seq, name, pwd)

    return redirect('/forumList')

# 포럼 댓글 등록
@forum.route('/forumCommentInsert', methods=['POST','GET'])
def ForumCommentInsert():

    print(request.values)
    seq = request.values.get("seq")
    cnts = request.values.get("cnts")

    forum_sql.ForumDao.insertForumComment(seq, cnts)

    return redirect('/forumDetail?seq='+seq)

# 포럼 댓글 등록
# @forum.route('/forumCommenmtInsertAjax', methods=['POST'])
# def forumCommenmtInsertAjax():

#     data = request.get_json()
#     print(data)

#     forum_sql.ForumDao.insertForumComment(data['seq'], data['cnts'])

#     commentList = forum_sql.ForumDao.selectListForumComment(data['seq'])

#     return jsonify(resultCode = "success", commentList=commentList)