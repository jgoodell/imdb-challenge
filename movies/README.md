# Overview
This is still very early on in the development phase. I wrote a very basic script which dumps select columns from the rows in the CSV into a SQLite DB under a single object type of Movie. I've begun development of a more rich data and mobject model with a M2M relationship between a movie and the movie's genres. I'm taking a object based approach to handling the data with SQLAlchemy and factory methods for creating the instances. Leap-before-loooking flow for handling duplicate entries (especially Genre).

# Next Steps
I would begin looking at pandas, but most of the calculations can easily be done using the database server as long the data after extract is transformed properly. I would finish the Genre model and add a presisted 'profit' attribute to the Movie object in prep for profitability by genre. I'd then begin working on an Actor model with a similar approach to the Genre model.

# Instructions
The only dependency for functionality is SQLAlchemy, but all of the dependencies can easily be installed by the following

  $ sudo pip3 install -r requirements.txt

From the same directory where this README.md is located. Place the data CSV in the directory movies/ To run the loader, change directories into movies/ and execute.

  $ python3 load_db.py

You can explore the 'movie' table in the database with sqlite3 by.

  $ sqlite3 movie.db