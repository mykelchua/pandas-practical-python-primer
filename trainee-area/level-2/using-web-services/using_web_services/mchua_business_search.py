"""
*** mchua***
This module interacts with a public Web API that provides business
listings.

The API docs are hosted at: http://api.searchcompany.us
"""

import requests

COMPANY_SEARCH_URL = "http://api.searchcompany.us/1.0/search"
COMPANY_RETRIEVAL_URL = "http://api.searchcompany.us/1.0/company"

def company_search(name: str):
    search_url = "{}/{}".format(COMPANY_SEARCH_URL, name)
    return requests.get(search_url).json()['company']   # Method Chaining

    # Without Method Chaining
    # results = requests.get(search_url)
    # json_payload = results.json()
    # company_records = json_payload['company']
    # return company_records

def companies_info(companies: list):
  company_ids = []   # Alternatively, company_ids = list()
  for company in companies:
        company_ids.append(company['id'])

  # Equivalent Using List Comprehension
  # company_ids = [
  #     company['id'] for company in results.json()['company']]


  company_information = []
  for company_id in company_ids:
        lookup_url = "{}/{}".format(
            COMPANY_RETRIEVAL_URL, company_id)
        lookup_results = requests.get(lookup_url)
        company_information.append(lookup_results.json())

        # Equivalent in 2 Statements
        # lookup_json = lookup_results.json()
        # company_information.append(lookup_json)
  return company_information

if __name__ == "__main__":
    company_list = company_search(name="Superman")
    company_information = companies_info(companies=company_list)
    #results = company_search(name="Panda")
    #print(company_information)


