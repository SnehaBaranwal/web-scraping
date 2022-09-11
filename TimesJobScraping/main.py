import time

from bs4 import BeautifulSoup
import requests

print('Put some skill you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/companySearchResult.html?from=submit&encid=cScjAb01ZdpKJWBivbjphQ==&searchType=byCompany&luceneResultSize=25').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            # print(type(skills))
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open (f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\ncl")
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')

if __name__=='__main__':
    # want to run this program forever
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        # To make the program refresh every 10 minutes we use time.sleep
        time.sleep(time_wait * 60)



