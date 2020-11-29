from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_surfing


app = Flask(__name__)

#use pyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# route to index using Mongo data
@app.route('/')
def index():
    mars = mongo.db.mars_app.find_one()
    
    return render_template('index.html')


@app.route('/scrape')
def scrape():
    mars_data = mongo.db.mars
    data = scrape_mars.scrape()
    mars_data.update(
        {},
        data
    )
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
