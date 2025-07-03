from flask import Blueprint, render_template
# Blueprintオブジェクトを生成する
crud = Blueprint(
    'crud',
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/crud'
)

# indexエンドポイントを作成しindex.htmlを返す
@crud.route('/')
def index():
    return render_template('crud/index.html')