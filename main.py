from selenium.webdriver import Chrome
import pandas as pd

webdriver = r"chromedriver.exe"
driver = Chrome(webdriver)

pages = 15

title = []
description = []
hospital = []
country = []
price = []
job_time = []
time = []
link_title = []
img = []

for page in range(1, pages + 1):
    url = 'https://www.carehome.co.uk/jobs/index.cfm/jobcategory/nurses/jobtype/full-time/startpage/' + str(page)

    driver.get(url)

    quotes = driver.find_elements_by_class_name("panel-body.row")
    for quote in quotes:
        title_text = quote.find_element_by_tag_name('span').text
        link_text = quote.find_element_by_tag_name('a').get_attribute("href")
        hospital_text = quote.find_element_by_tag_name('strong').text
        country_text = quote.find_element_by_class_name('col-sm-4.home-price').text
        description_text = quote.find_element_by_class_name('hidden-xs').text
        img_url = quote.find_element_by_xpath("//img[@class='lazyload']").get_attribute("src")
        # Price
        col_sm_8 = quote.find_elements_by_class_name('col-sm-8.home-name')
        price_text = col_sm_8[0].text.split('\n')[2].split('•')[0].strip('( ')
        # Job
        job_time_text = col_sm_8[0].text.split('\n')[2].split('•')[-1].strip(') ')
        # Time
        col_sm_3 = quote.find_elements_by_class_name('col-sm-3.home-agent')
        time_post = col_sm_3[0].text

        title.append(title_text)
        hospital.append(hospital_text)
        country.append(country_text)
        price.append(price_text)
        job_time.append(job_time_text)
        description.append(description_text)
        time.append(time_post)
        link_title.append(link_text)
        img.append(img_url)

    df = pd.DataFrame({
        'Title': title,
        'Link Title': link_title,
        'Description': description,
        'Hospital': hospital,
        'Country': country,
        'Price': price,
        'Job Time': job_time,
        'Pictures': img
    })
    df.to_excel('./quoted.xlsx', sheet_name='Nursing - Care Homes', index=False)
driver.close()
print('Parsing completed successfully!')