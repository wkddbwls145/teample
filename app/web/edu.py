from cgi import test
from re import T
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

edu = Blueprint('edu', __name__, url_prefix='/')

# 학습메뉴


@edu.route('/edu001', methods=['POST', 'GET'])
def Edu001():
    return render_template('/web/edu/edu001.html')


@edu.route('/edu002', methods=['POST', 'GET'])
def Edu002():
    return render_template('/web/edu/edu002.html')


@edu.route('/edu003', methods=['POST', 'GET'])
def Edu003():
    return render_template('/web/edu/edu003.html')


@edu.route('/edu004', methods=['POST', 'GET'])
def Edu004():
    return render_template('/web/edu/edu004.html')


@edu.route('/edu005', methods=['POST', 'GET'])
def Edu005():
    return render_template('/web/edu/edu005.html')


@edu.route('/edu006', methods=['POST', 'GET'])
def Edu006():
    return render_template('/web/edu/edu006.html')


@edu.route('/edu007', methods=['POST', 'GET'])
def Edu007():
    return render_template('/web/edu/edu007.html')


@edu.route('/edu008', methods=['POST', 'GET'])
def Edu008():
    return render_template('/web/edu/edu008.html')


@edu.route('/edu009', methods=['POST', 'GET'])
def Edu009():
    return render_template('/web/edu/edu009.html')


@edu.route('/edu010', methods=['POST', 'GET'])
def Edu010():
    return render_template('/web/edu/edu010.html')


@edu.route('/edu011', methods=['POST', 'GET'])
def Edu011():
    return render_template('/web/edu/edu011.html')


@edu.route('/edu012', methods=['POST', 'GET'])
def Edu012():
    return render_template('/web/edu/edu012.html')


@edu.route('/edu013', methods=['POST', 'GET'])
def Edu013():
    return render_template('/web/edu/edu013.html')


@edu.route('/edu014', methods=['POST', 'GET'])
def Edu014():
    return render_template('/web/edu/edu014.html')


@edu.route('/edu015', methods=['POST', 'GET'])
def Edu015():
    return render_template('/web/edu/edu015.html')


@edu.route('/edu016', methods=['POST', 'GET'])
def Edu016():
    return render_template('/web/edu/edu016.html')


@edu.route('/edu017', methods=['POST', 'GET'])
def Edu017():
    return render_template('/web/edu/edu017.html')


@edu.route('/edu018', methods=['POST', 'GET'])
def Edu018():
    return render_template('/web/edu/edu018.html')
