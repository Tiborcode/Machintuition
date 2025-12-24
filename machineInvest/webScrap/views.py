from django.shortcuts import render, redirect

from .forms import BalanceSheetuploadForm, CashFlowUploadForm, IncomeStatementUploadForm


# Create your views here.
def startpage(request):


    return render(request, 'webScrap/startpage.html')

def uploadpage(request):
    cashForm = CashFlowUploadForm
    incomeForm = IncomeStatementUploadForm
    balanceForm = BalanceSheetuploadForm

    return render(request, 'webScrap/uploadpage.html', {'cashForm': cashForm, 'incomeForm':incomeForm, 'balanceForm': balanceForm})