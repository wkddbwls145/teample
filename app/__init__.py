from flask import Flask

app = Flask(__name__)

# 파일 이름이 index.py이므로
from app.web.main import main as main 
from app.web.edu import edu as edu # 학습메뉴
from app.web.quiz import quiz as quiz # 테스트메뉴
from app.web.forum import forum as forum # 개발자 포럼

# 위에서 추가한 파일을 연동해주는 역할
app.register_blueprint(main) # as main으로 설정해주었으므로
app.register_blueprint(edu)
app.register_blueprint(quiz)
app.register_blueprint(forum)