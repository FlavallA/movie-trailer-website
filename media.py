import fresh_tomatoes
import movie

def readInMovie(f):
    title = f.readline()
    posterurl = f.readline()
    trailerurl = f.readline()

    # check to make sure we have info to create a movie
    if title and posterurl and trailerurl:
        return movie.Movie(title, posterurl, trailerurl)
    else:
        return None

# open file with movie info in a way that will happen closing automagically
with open("MovieInfo.txt") as f:
    Movies = []

    # read in the info for the first movie
    Movies.append(readInMovie(f))
    # read the empty lone between movies or detect the end of the file
    while f.readline():
        # read in the info for the next movie
        Movies.append(readInMovie(f))

    # create the webpage
    fresh_tomatoes.open_movies_page(Movies)
    
    
    
