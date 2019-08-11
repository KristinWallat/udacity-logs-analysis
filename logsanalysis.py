import psycopg2

DBNAME = "news"


# 1st question query
def get_popular_articles(num):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select articles.title, subq.views from articles join
        (select right(path, -9), count(*) as views from log where
        status='200 OK' and path like '/article/%%' group by path
        order by views desc limit %d) as subq on articles.slug=subq.right
        order by subq.views desc""" % num)
    stat = c.fetchall()
    db.close()
    print("\n%d most popular articles of all time are: " % num)
    for item in stat:
        print(str(item[0]) + '" - ' + str(item[1]) + " views")


# 2nd question query
def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""select authors.name, sub.views from authors join
        (select articles.author, sum(subq.views) as views from articles join
        (select right(path, -9), count(*) as views from log where
        status='200 OK' and path like '/article/%' group by path)
        as subq on articles.slug=subq.right group by articles.author
        order by articles.author) as sub on authors.id=sub.author""")
    stat = c.fetchall()
    db.close()
    print("\nMost popular article authors of all time are: ")
    for item in stat:
        print(str(item[0]) + " - " + str(item[1]) + " views")


# 3rd question query
def get_errors(rate):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # refer to README.md for query to create stat view
    c.execute("""select date, errors*100/total as error_percentage
        from stat where (errors*100/total) >= (%d)""" % rate)
    stat = c.fetchall()
    db.close()
    print("\nOn the following dates more that %d %% of requests "
          "lead to errors: " % rate)
    for item in stat:
        print(str(item[0]) + " - " + str(item[1]) + "%")

get_popular_articles(3)
get_popular_authors()
get_errors(1)