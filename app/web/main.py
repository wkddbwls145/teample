from cgi import test
from re import T
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')


@main.route('/', methods=['GET'])
def Main():
    # /main/index.html은 사실 /project_name/app/templates/web/main.html을 가리킵니다.

    # GET 방식
    parameter_dict = request.args.to_dict()

    # POST 방식
    #request.form.get("article", "1", int)
    #parameters = request.form

    # GET, POST 둘다 수용
    # request.values.get("name")
    parameters = request.values

    # if len(parameter_dict) == 0:
    #parameters = 'No parameter'

    # for key in parameter_dict.keys():
    #parameters += 'key: {}, value: {}\n'.format(key, request.args[key])

    return render_template('/web/main.html')
