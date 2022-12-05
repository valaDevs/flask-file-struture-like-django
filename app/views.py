from app import app 
from flask import render_template , request , redirect , make_response , jsonify

@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/jinja')
def jinja():

    name = "gholam"

    age = 21

    langs = ['Python', 'javascript','ruby','Golang','Bash']

    friends = {
        'Tom':50, 
        'Susi':30, 
        'Bob':23, 
        'Tony':20, 
    }

    colors = ("Purple",'Green', "Black")
    
    cool = True

    class Gitremote:
        def __init__(self,name,description,url):
            self.name = name 
            self.description = description
            self.url = url
        
        def pull(self):
            return f"Pulling Repo {self.name} "
        def clone(self):
            return f"Cloning Into {self.url}"

    my_remote = Gitremote('flask-blog','simlple flask blog project','https://github.com/valaDevs/flask_blog.git')

    def repeat(x,qty):
        return x * qty

    return render_template('/public/jinja.html',
     name=name,
     age = age,
     langs=langs,
     friends=friends,
     colors = colors,
     cool=cool,
     Gitremote=Gitremote,
     repeat = repeat,
     my_remote=my_remote

     )

@app.route("/about")
def about():
    return "<h1>About US !!!!!!!!! </h1>"



@app.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        req = request.form 
        
        username = req['username']
        email = req.get('email')
        password = request.form['password']

        print(username,email,password)

        return redirect(request.url)

    return render_template('public/signup.html')


users = {

    "valakonos": {
        "name": "vala",
        "bio": "i dont give a fuck",
        'twitter': "@vala"
    },
       "quala": {
        "name": "kire",
        "bio": "at sleep",
        'twitter': "@dsees"
    },

       "kaboos": {
        "name": "konos",
        "bio": "life is a joke",
        'twitter': "@kaboos"
    },

}
    
@app.route('/profile/<username>')
def profile(username):

    user = None
    if username in users:
        user = users[username]
     
    return render_template('public/profile.html',username=username,user=user)


@app.route('/multiple/<foo>/<bar>/<baz>')
def multiple(foo,bar,baz):
    return f"foo is {foo} bar is{bar} baz is{baz}"


@app.route('/json',methods=['POST'])
def json():

    if request.is_json: 
        req = request.get_json()

        response = {
            "message" : "JSON Received ! ok",
            "name" : req.get('name')

        }
        res = make_response(jsonify(response),200)

        return res

    else:

        res = make_response(jsonify({"message" : "No JSON Was Received !!"}),400)
        return res


@app.route('/guestbook')
def guestbook():
    return render_template('public/guestbook.html')


@app.route('/guestbook/create-entry', methods=["POST"])
def create_entry():

    req = request.get_json()
    print(req)

    res = make_response(jsonify({"message":"JSON Received"}),200)

    return res


@app.route('/query')
def query():
    args = request.args
    if "foo" in args:
        foo = args.get('foo')
        print(foo)

    elif request.args:
        serialized = ", ".join(f"{k}: {v}"for k,v in arg.items())

    return "Query was received", 200

