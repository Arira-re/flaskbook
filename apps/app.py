from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
# SQLAlchemyをインスタンス化する
db = SQLAlchemy()
csrf = CSRFProtect()
login_manager = LoginManager()

login_manager.login_view = "auth.signup"
login_manager.login_message = ""


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
    login_manager.init_app(app)
    # crudパッケージからviewsをインポートする
    from apps.crud import views as crud_views
    from apps.auth import views as auth_views
    from apps.detector import views as dt_views
    # register_blueprintを使いcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix='/crud')
    app.register_blueprint(auth_views.auth, url_prefix='/auth')
    app.register_blueprint(dt_views.dt)
    return app
