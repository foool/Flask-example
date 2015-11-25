from flask import Flask, url_for, redirect, render_template, request
from math import ceil
from pagination import Pagination



app = Flask(__name__)
app.debug = True

PER_PAGE = 20

@app.route('/users/', defaults={'page': 1})     ###
@app.route('/users/page/<int:page>')
def show_users(page):
    count = 601
    users = ['name']*20
    if not users and page != 1:
        abort(404)
    pagination = Pagination(page, PER_PAGE, count)
    return render_template('pagination2.html', pagination=pagination)


@app.route('/')
def index():
    return redirect(url_for('rank'))

def url_for_other_page(page):       ###
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page ###

if __name__ == '__main__':
    app.run()
