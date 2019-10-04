
import psycopg2


connection = psycopg2.connect("dbname=news")
c = connection.cursor()



def draw_line(numbers: int = 15 , character: str = ' _'):
    print(character * numbers)



def most_popular_articles():
    c.execute('''SELECT a.title, COUNT(*) as view_articles
        FROM articles as a
        join log 
        ON log.path LIKE concat('/article/%', a.slug)
        GROUP BY a.title
        ORDER BY view_articles DESC LIMIT 3;''')
    result = c.fetchall()

    for (title, view) in result:
        print(" {} = {} views.".format(title, view))
    



def most_popular_article_authors():
    c.execute('''SELECT au.name, COUNT(*) as view_authors
        FROM authors as au
        join articles as a 
        join log 
        WHERE a.author = au.id AND log.path = concat('/article/', a.slug)
        GROUP BY au.name
        ORDER BY view_authors DESC;''')
    result = c.fetchall()

    for (name, view) in result:
        print(" {} = {} views.".format(name, view))
  


def define_error():
    c.execute(''' SELECT * FROM percentage_errors WHERE percentage > 1
    ORDER BY percentage_errors.percentage DESC;''')

    result = c.fetchall()
    for (date, percentage) in result:
        print("   {} - {}% Errors".format(date, percentage))
    



if __name__ == "__main__":
    print("What are the most popular three articles of all time?")
    most_popular_articles()
    draw_line()
    print("")

    print("2. Who are the most popular article authors of all time? ")
    most_popular_article_authors()
    draw_line()

    print("3. On which days did more than 1% of requests lead to errors?")    
    define_error()
    draw_line()
    print("")

    # exit connection with the database
    c.close()
    connection.close()

