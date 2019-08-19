#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# 1st question query: What are the most popular articles of all times?


def get_popular_articles(num):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """select title, count(path) from articles, log
                where status like '200%'
                and concat('/article/', articles.slug) = log.path
                group by title
                order by count(path) desc
                limit 4""")
    c_records = c.fetchall()
    db.close()
    print("4 most popular articles are: ")
    for row in c_records:
        print("\"" + row[0] + "\" - " + str(row[1]) + " views")


# 2nd question query: What are the most popular authors of all times?
def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """select authors.name, count(*)
            from articles inner join
            authors on articles.author = authors.id
            inner join log on
            concat('/article/', articles.slug) = log.path
            where log.status like '200%'
            group by authors.name
            order by count(log.path) desc""")
    c_records = c.fetchall()
    db.close()
    print("\nMost popular article authors are: ")
    for row in c_records:
        print("\"" + row[0] + "\" - " + str(row[1]) + " views")

# 3rd question query:On which days did more than 1% of requests lead to errors?


def get_errors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(
        """select cast((stat*100.00)/visitors as varchar(4)) as\n
        result, TO_CHAR(errortime, 'Mon DD,YYYY')\n
        FROM error_days ORDER BY result desc limit 1""")
    c_records = c.fetchall()
    db.close()
    print("\nOn this day more than 1% of requests led to an error:")
    for k in c_records:
            print (str(k[0]) + "%" + "--" + str(k[1]))

get_popular_articles(3)
get_popular_authors()
get_errors()
