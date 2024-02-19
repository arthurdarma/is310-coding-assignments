# favorite_movies =[
#     {
#         "name": "The Matrix I",
#         "release_year": 1999,
#         "sequels": ["The Matrix II", "The Matrix III", "The Matrix IV"]
#     },
#     {
#         "name": "Star Wars IV",
#         "release_year": 1977,
#         "sequels": ["Star Wars V", "Star Wars VI", "Star Wars VII", "Star Wars VIII", "Star Wars IX"],
#         "prequels": ["Star Wars I", "Star Wars II", "Star Wars III"]
#     }
# ]
# print('Enter your favorite movie of the last year:') 
# recent_favorite_movie = input('Enter your favorite movie of the last year:')
# print('Your favorite movie is of the last year:', recent_favorite_movie)
# favorite_movies[0]['long_description'] = "The Matrix is a 1999 science fiction action film written and directed by the Wachowskis. It is the first installment in The Matrix film series, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano. The Waschowskis created a plot set in a dystopian future where humanity is unknowingly trapped inside a simulated reality, the Matrix, created by intelligent machines to distract humans while using their bodies as an energy source. In the movie, the main character, Neo, is a computer programmer who learns this truth and is drawn into a rebellion against the machines, which involves other people who have been freed from the Matrix."
# print(favorite_movies[0])
# split_description = favorite_movies[0]['long_description'].split(' ')
# print(split_description)
# print(len(split_description))
# favorite_movies[0]['short_description'] = ' '.join(split_description[:10])
# print(favorite_movies[0]['short_description'])
# print(' '.join(split_description))

# edited_description = favorite_movies[0]['long_description'].replace('the Wachowskis', 'Lana and Lilly Wachowski')
# print(edited_description)
# for movie in favorite_movies:
#     print(movie['name'])

# individual_movie = favorite_movies[0]
# for key, value in individual_movie.items():
#     print(key, value)   

# first_movie_name = favorite_movies[0]['name']
# for letter in first_movie_name:
#     print(letter)

# def print_movie_name_and_year(movie):
#     movie_data = movie['name'] + ' was released in ' + str(movie['release_year'])
#     print(movie_data)

# print_movie_name_and_year(favorite_movies[1])

# if not favorite_movies[0]['release_year'] > 1999:
#     print('The Matrix')
# else:
#     print('Star Wars')

# if favorite_movies[0]['sequels'] is not None:
#     print('Sequels')
# else:
#     print('No Sequels')

from pathlib import Path

current_directory = Path.cwd()
print(current_directory)


#file = Path('/mnt/c/Users/arthu/Downloads/pudding_data.csv.csv')
file = Path('../Downloads/pudding_data.csv.csv')

print(file, type(file))
print(file.read_text())

# input_file = open("pudding_data.csv","r")
# text = input_file.read()
# print(text)
# input_file.close()

# with open("pudding_data.csv","r") as input_file:
#     print(input_file.read())

f = open("new_text.txt","w")
for i in range(0,100):
    f.write(str(i**2)+"\n")

import csv

with open("pudding_data.csv","r") as input_file:
    csv_reader = csv.reader(input_file)
    for row in csv_reader:
        print(row)