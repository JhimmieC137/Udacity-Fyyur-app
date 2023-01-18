import dateutil.parser
import babel
import json
import sys
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *


# from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    # genres = db.relationship('Genre', secondary=genre_list, backref='Music_style')
    genres = db.Column(db.ARRAY(db.String(120)))
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    website = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(200))
    # programs = db.relationship("Shows", backref = "venues", lazy=False, cascade="all, delete-orphan")
    past_shows = db.Column(db.String())
    upcoming_shows = db.Column(db.String())
    past_shows_count = db.Column(db.Integer)
    upcoming_shows_count = db.Column(db.Integer)
    
    
class Artist(db.Model):
    __tablename__ = 'Artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    # genres = db.relationship('Venue',secondary=, backref=db.backref('Singers', lazy=True))
    genres = db.Column(db.ARRAY(db.String(120)))
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(500))
    past_shows = db.Column(db.String())
    upcoming_shows = db.Column(db.String())
    past_shows_count = db.Column(db.Integer)
    upcoming_shows_count = db.Column(db.Integer)
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(200))
    # concerts = db.relationship("Shows", backref = "artists", lazy=False, cascade="all, delete-orphan")
    
    def __repr__(self):
      return f'<Artist ID: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, phone: {self.phone}, image_link: {self.image_link}, facebook: {self.facebook_link}>'
    
    
class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    venue_id = db.Column(db.Integer, db.ForeignKey('Venues.id'))
    venue_name = db.Column(db.String())
    artist_id = db.Column(db.Integer, db.ForeignKey('Artists.id'))
    artist_name = db.Column(db.String())
    artist_image_link = db.Column(db.String())
    venue_image_link = db.Column(db.String())
    start_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)