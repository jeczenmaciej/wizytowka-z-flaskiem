from flask import Flask, request

app = Flask(_name_)

@app.route('/mypage/me')
def about_me():
    return "Tutaj znajdują się informacje o mnie."

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form.get('message')
        print(f"Wiadomość od użytkownika: {message}")
        return "Dziękuję za wiadomość!"
    else:
        return "Tutaj znajdują się moje informacje kontaktowe."

if _name_ == "_main_":
    app.run(debug=True)