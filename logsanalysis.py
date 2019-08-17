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
    c_records = c.fetchall()
    db.close()
    print("\n%d most popular articles of all time are: " % num)
    for item in c_records:
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
    c_records = c.fetchall()
    db.close()
    print("\nMost popular article authors of all time are: ")
    for item in c_records:
        print(str(item[0]) + " - " + str(item[1]) + " views")


# 3rd question query
def get_errors(rate):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    # see READme to create Views
    c.execute("select REPLACE(TO_CHAR(time,'Month DD,YYYY'),'      ',' ') \
           as days,((requests_errors*100)/count(status)::float) as Percent\
           from log,requests_errors where TO_CHAR(time,'Month DD,YYYY')= \
           day group by (days,requests_errors) having ((requests_errors*100) \
           /count(status))>1;")
    c_records = c.fetchall()
    db.close()
    print("On these days did more than 1 percent of requests lead to errors:\
        " + "\n")
    for row in c_records:
        print("* " + str(row[0]) + " -- " + str(round(row[1], 2)) + "% errors")



get_popular_articles(3)
get_popular_authors()
get_errors(1)