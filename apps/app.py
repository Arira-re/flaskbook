from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
# SQLAlchemyをインスタンス化する
db = SQLAlchemy()
csrf = CSRFProtect()
def create_app():
    # Flaskインスタンス作成
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='abcdef',
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SQLをコンソールログに出力する設定
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY='abcdef'
    )
    csrf.init_app(app)
    # SQLAlchemyをアプリにバインドするを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    migrate = Migrate(app, db)
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    # register_blueprintを使いcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    return app