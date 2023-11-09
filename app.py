from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 멤버와 책 데이터를 저장할 딕셔너리 생성
members = {}
books = {}

@app.route('/')
def index():
    # 웹 페이지에 멤버 정보와 책 상태 정보 표시
    return render_template('index.html', members=members, books=books)

@app.route('/add_member', methods=['POST'])
def add_member():
    # 멤버 추가 기능 구현
    member_name = request.form['member_name']
    member_phone = request.form['member_phone']
    members[member_name] = member_phone
    return redirect(url_for('index'))


@app.route('/remove_member', methods=['POST'])
def remove_member():
    # 멤버 삭제 기능 구현
    member_name = request.form['member_name']
    if member_name in members:
        del members[member_name]
	print(Hello)
    return redirect(url_for('index'))

@app.route('/add_book', methods=['POST'])
def add_book():
    # 책 추가 기능 구현
    book_name = request.form['book_name']
    books[book_name] = 'available'
    return redirect(url_for('index'))

@app.route('/remove_book', methods=['POST'])
def remove_book():
    # 책 삭제 기능 구현
    book_name = request.form['book_name']
    if book_name in books:
        del books[book_name]
    return redirect(url_for('index'))

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    # 책 대출 기능 구현
    book_name = request.form['book_name']
    if book_name in books and books[book_name] == 'available':
        books[book_name] = 'borrowed'
    return redirect(url_for('index'))

@app.route('/return_book', methods=['POST'])
def return_book():
    # 책 반납 기능 구현
    book_name = request.form['book_name']
    if book_name in books and books[book_name] == 'borrowed':
        books[book_name] = 'available'
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
