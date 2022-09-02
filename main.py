from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # Grabbing some specific information (here we are getting the info from h5 tags)
    # tags = soup.find('h5')
    # print(tags)  # O/P: <h5 class="card-title">Python for beginners</h5> (but we have more than 1 h5 tags)
    # .find() just searches for the first element and then stops searching
    # That's why we use the .find_all()
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)
    # We get all the h5 from the home.html document
    # for course in courses_html_tags:
    #    print(course.text)
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')


