# Create a class named as Movie

class Movie:
    """Movie class developed for basic oop demo purpose"""
    def __init__(self,title,hero,genre):
        self.title = title
        self.hero = hero
        self.genre = genre

    # Method for printing information
    def info(self):
        print("The title of the movie is: ",self.title)
        print("The hero of the movie is: ",self.hero)
        print("The movie genre is: ",self.genre)


# Get the movies list

# Create an empty list
Movies_list = []
while True:
    title = input("Enter the movie title: ")
    hero = input("Enter the hero name: ")
    genre = input("Enter the movie genre: ")
    obj1 = Movie(title,hero,genre)
    Movies_list.append(obj1)
    print("Movie added to the list successfully")

    # Check whether user wants to add more movies?
    option = input("Do you want to add more movies? [Yes (or) No]")
    if option.lower() == 'no':
        break

print("All Movies information")
print("#"*40)

for movies in Movies_list:
    movies.info()
    print()