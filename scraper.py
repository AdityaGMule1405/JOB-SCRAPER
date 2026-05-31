from bs4 import BeautifulSoup
import csv

def scrape_jobs(html_file, output_csv):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    job_listings = []
    for job_div in soup.find_all('div', class_='job'):
        title = job_div.find('h2').get_text(strip=True)
        salary_text = job_div.find('p').get_text(strip=True)
        salary = int(salary_text.split(':')[-1].strip())

        if 10000 <= salary <= 15000:
            job_listings.append({'Title': title, 'Salary': salary})

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for job in job_listings:
            writer.writerow(job)

if __name__ == '__main__':
    scrape_jobs('mock_board.html', 'leads.csv')
