from django.shortcuts import render, redirect
#from .getdata import FinancialStatementScraper, YahooFinanceClient


# Create your views here.
def startpage(request):


    return render(request, 'webScrap/startpage.html')
