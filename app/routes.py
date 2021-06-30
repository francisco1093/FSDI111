from app import app # From our app package import the app variable

@app.route("/") #A decoratior that maps paths to view functions
def hello():    # View function
    return "<h1>Hello World</h1>" # A simple return statement


@app.route("/about")
def about():
    me = {
        "first_name":"Francisco",
        "last_name":"Cardenas",
        "hobby":"Chess",
        "ok":True
    }
    return me
