import csv
from Author import Author
from Work import Work

# with open('./inputList/authorTest.csv', 'r', encoding='utf8') as au:
#     reader = csv.reader(au)
#     authors = []
#     for row in reader:
#         author = Author(str(row[0]))
#         print(type(author.name))
#         authors.append(author)
#     print(authors)

with open('./inputList/workTest.csv', 'r', encoding='utf8') as au:
    reader = csv.reader(au)
    works = []
    for row in reader:
        work = Work(str(row[0]))
        print(work.wid)
        works.append(work)
    # print(works)

