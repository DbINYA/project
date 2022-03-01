from flask import Flask
from data.users import User
from data import db_session

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/blogs.sqlite")
    db_sess = db_session.create_session()
    print(db_sess.query(User).first().name)
    # 7 пункт, все юзеры уже сделаны
    # app.run()


if __name__ == '__main__':
    main()
