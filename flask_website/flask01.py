from flask import Flask,render_template

app= Flask(__name__)

posts_author=[
       {
        'author':'Brian',
        'title':'WorkBook Blog1',
        'content':'Content of the workbook',
        'date_posted':'June 21,2019'
       },
       {
        'author':'Kolby',
        'title':'WorkBook Blog2',
        'content':'Content of the workbook22',
        'date_posted':'August 17,2019'
        }
       
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html',posts=posts_author)
#app.add_url_rule('/', 'hello', home)

@app.route("/about")
def about():
    return render_template('About.html',title='About')

if __name__=='__main__':
    app.run(debug=True)