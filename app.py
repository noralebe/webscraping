from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")




@app.route("/scrape")
def scrape():

    # Run the scrape function
    # mars=mongo.db.mars
    mars_all_scraped = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_all_scraped, upsert=True)

    # Redirect back to home page
    return redirect("/")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    destination_data = mongo.db.collection.find_one()
    # collection = db.all_scraped
    # mars=mongo.db.collection.find()[0]
    # destination_data = mongo.db.mars_app.collection.twitter_mars.find())
    print(destination_data)
    # mars_data = list(mongo.db.mars_pp.mars.find())
    # mars_data=mongo.db.mars_app.mars.find({"paragraph"})
    # mars_all_scraped = scrape_mars.scrape_info()

    # Return template and data
    return render_template("index.html", mars=destination_data)

if __name__ == "__main__":
    app.run(debug=True)
