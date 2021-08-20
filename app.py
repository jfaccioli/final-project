import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///keyword_clustering.sqlite")
conn = engine.connect()

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

########## Home Page ########## 

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to SEO Keyword Clusters<br/>"
        f"Available Routes:<br/>"
        f"/keyword_clustering_data<br/>"
    )


########## Keyword Clustering ##########

# Query our keyword clustering data
keyword_clustering_data = pd.read_sql("SELECT * FROM keyword_clustering", conn)

@app.route("/keyword_clustering_data")
def keyword_clustering():
    return jsonify(keyword_clustering_data.to_dict())


if __name__ == '__main__':
    app.run(debug=True)