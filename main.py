from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")
articles = soup.find_all(name="h3", class_="title")
# print(articles)
article_text = []
for article in articles:
    text = article.getText()
    article_text.append(text)

article_text.reverse()
with open("movies.txt", mode='w') as file:
    for article in article_text:
        file.write(article)
        file.write("\n")

# for article in article_text:
#     print(article)

# print(article_text)
#
# movie_number1 = [article.getText().split(")")[0] for article in articles]
# number = movie_number1[-12].split(":")[0]
# movie_number1[-12] = number
# movie_number =[]
# for number in movie_number1:
#     number = int(number)
#     movie_number.append(number)
# movie_number.reverse()
#
# # print(movie_number)
# numbers = max(movie_number)
# number_index = movie_number.index(numbers)
# print(article_text[number_index])
# # for n in movie_number:
#
# print(article_text)
# print(movie_number)
# print(numbers)
# print(number_index)



# for article_text in numbers:
#     movies_top.append(article_text[number_index])
#
# print(movies_top)