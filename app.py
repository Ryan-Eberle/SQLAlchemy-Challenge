
# dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# database set up
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station


# Flask Set Up

app = Flask(__name__)

# Set up Flask routes 


@app.route("/")
def weclome():
	return (
		f"Aloha, Available Routes:<br/>"
		f"Precipitation: /api/v1.0/precipitation<br/>"
		f"List of our Stations: /api/v1.0/stations<br/>"
		f"Temperature for the past year: /api/v1.0/tobs<br/>"
		f""






		)
