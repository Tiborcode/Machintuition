import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Dict



HEADERS = {"User-Agent": "tkelemen33@gmail.com"}
def cik_matching_ticker(ticker, headers=HEADERS):
    ticker = ticker.upper().replace(".", "-")
    ticker_json = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    ).json()

    for company in ticker_json.values():
        if company["ticker"] == ticker:
            cik = str(company["cik_str"]).zfill(10)
            #print(cik)
            return cik
    raise ValueError(f"Ticker {ticker} not found in SEC database")

#cik_matching_ticker("oxy")

def get_submission_data_for_ticker(ticker, headers=HEADERS, only_filings_df=False):
    """
    Get the data in json form for a given ticker. For example: 'cik', 'entityType', 'sic', 'sicDescription', 'insiderTransactionForOwnerExists', 'insiderTransactionForIssuerExists', 'name', 'tickers', 'exchanges', 'ein', 'description', 'website', 'investorWebsite', 'category', 'fiscalYearEnd', 'stateOfIncorporation', 'stateOfIncorporationDescription', 'addresses', 'phone', 'flags', 'formerNames', 'filings'

    Args:
        ticker (str): The ticker symbol of the company.

    Returns:
        json: The submissions for the company.

    Raises:
        ValueError: If ticker is not a string.
    """
    cik = cik_matching_ticker(ticker)
    headers = headers
    url = f"https://data.sec.gov/submissions/CIK{cik}.json"
    company_json = requests.get(url, headers=headers).json()
    if only_filings_df:
        #print("1")
        #print(pd.DataFrame(company_json["filings"]["recent"]))
        return pd.DataFrame(company_json["filings"]["recent"])
    else:
        #print("2")
        #print(company_json)
        return company_json
#data = get_submission_data_for_ticker("oxy", only_filings_df=False)
#print(data.keys())


def get_filtered_filings(
    ticker, ten_k=True, just_accession_numbers=False, headers=HEADERS):
    company_filings_df = get_submission_data_for_ticker(
        ticker, only_filings_df=True, headers=headers
    )
    if ten_k:
        print("a")
        df = company_filings_df[company_filings_df["form"] == "10-K"]
    else:
        print("b")
        df = company_filings_df[company_filings_df["form"] == "10-Q"]
    if just_accession_numbers:
        print("c")
        df = df.set_index("reportDate")
        accession_df = df["accessionNumber"]
        return accession_df
    else:

        return df

filings = get_filtered_filings("oxy", ten_k=False, just_accession_numbers=True, headers=HEADERS)
#print(filings)