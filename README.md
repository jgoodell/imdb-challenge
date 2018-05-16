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

# Challenge
The following is an IMDB movie dataset available via Kaggle https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset/data.
 
The column names in this dataset should be more or less self-descriptive. Some of the key columns that pertain to this mini-project are: ‘actor_1_name’, ‘actor_2_name’, ‘actor_3_name’, ‘director_name’, ‘budget’ and ‘gross’. You can make assumptions about these names as you see fit in case they do not seem descriptive enough.
 
The task requires the following:
Import the file into a local db
Then write functions in python to perform the following computations on this dataset. (Feel free to use pandas for this purpose):
Compute the top 10 genres in decreasing order by their profitability. Note: You could compute profitability as simply as:
‘gross’ - ’budget’ or
(‘gross’ - ‘budget’)/’budget’
Anything advanced that you can think of
Return the top 10 actors or directors in decreasing order by their profitability (use any definition you choose for profitability using the above guidance).
Bonus questions (Note: If you choose to do any of the bonus questions below, any one question is more than adequate):
Choice 1: Find the best actor, director pairs (up to 10) that have the highest IMDB_ratings, if there are indeed any such pairs.
Choice 2: Any interesting questions that you would like to work on if you would  (for e.g. imdb_score, actor facebook_likes
Choice 3: Build a REST API to return an actor’s information (simple text output)
Write tests for your functions.
Commit code to a git repo (gitlab or github) and send us a link to it.
Also document your steps, libraries used and any instructions.
 
