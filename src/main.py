from bs4 import BeautifulSoup

#we created a statement that go and open the html file and give all the statement in a var called html_file
#'r', means read that file
with open('../html/home.html', 'r') as html_file:
    content = html_file.read()#content var equal to what html_file.read is wich is reading the content of home.html

    #we'eve created an instance of BeautifulSoup() wich contains the content of html file and the parser as a second parameter
    soup = BeautifulSoup(content, 'lxml')#lxml is an html parser into python objects
    course_cards = soup.find_all('div', class_='card')

    for course in course_cards:
        course_name = course.h5.text
        # course_price = course.a.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')

    # course_html_tags = soup.find_all('h5') #find finds just the first h5 element no as find_all

    #a loop that iterate thru all course_html_tags elemements and then instead fo writing everything we print only the content
    # for course in course_html_tags:
    #    print(course.text)


    # print(course_html_tags)

    #  print(soup.prettify())#prettify is to make the html code more beutifull more pretty