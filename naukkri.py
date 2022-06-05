import requests
import pandas as pd

url = "https://www.naukri.com/jobapi/v3/search"
data = []
final_output = pd.DataFrame(columns=['Title','Company','Skills','URL','Description','Experience','salary','Location'])
for x in range(1,6):

    querystring = {"noOfResults":"20","urlType":"search_by_key_loc","searchType":"adv","keyword":"data analyst","location":"bangalore/bengaluru","pageNo":f"{x}","k":"data analyst","l":"bangalore/bengaluru","seoKey":"data-analyst-jobs-in-bangalore-bengaluru","src":"jobsearchDesk","latLong":"12.9859584_77.6404992"}

    headers = {    
        'authority': "www.naukri.com",
        'accept': "application/json",
        'accept-language': "en-US,en;q=0.9",
        'appid': "109",
        'cache-control': "no-cache",
        'clientid': "d3skt0p",
        'content-type': "application/json",
        'gid': "LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE",
        'referer': "https://www.naukri.com/data-analyst-jobs-in-bangalore-bengaluru?k=data%20analyst&l=bangalore%2Fbengaluru",
        'systemid': "109",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    jobs= response.json()
    
    for job in jobs["jobDetails"]:
        job_title = job['title']
        company_name = job['companyName']
        skills_required = job['tagsAndSkills']
        # others = job['placeholders']
        job_url = job['jdURL']
        job_description = job['jobDescription']
        others =[]
        for data in job["placeholders"]:
                others.append(data["label"])
        experience = others[0]
        salary = others[1]
        location = others[2]
        final_output = final_output.append({ 'Title':job_title, 'Company': company_name, 'Skills': skills_required, 'URL':job_url, 'Description':job_description,'Experience': experience,'salary':salary,'Location':location},ignore_index=True)
      
final_output.head()
final_output.to_excel("jobs_scrapped.xlsx", index=False )
        
