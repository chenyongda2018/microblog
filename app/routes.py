from flask import render_template,flash,redirect,get_flashed_messages,url_for
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # 当提交表单时，收集表单数据，对每个字段进行验证，当每个字段都正确时
    # 返回True
    # 只要有一个字段不符合，就返回False
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Cyd'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html', user=user, posts=posts)
