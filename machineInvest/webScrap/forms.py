from django import forms


class BalanceSheetuploadForm(forms.Form):
    ticker = forms.CharField(max_length=5, required=True, initial='TICKER')
    year = forms.DateTimeField()
    scale = forms.IntegerField(max_value=1000000)
    cashAndShortTermInv = forms.IntegerField()
    receivables = forms.IntegerField()
    inventory = forms.IntegerField()
    totalCurrentAsset = forms.IntegerField()
    netPropertyPlantEquipm = forms.IntegerField()
    totalAssets = forms.IntegerField()
    currentLiabilities = forms.IntegerField()
    longTermLiabilities = forms.IntegerField()
    commonEquity = forms.IntegerField()
    totalEquity = forms.IntegerField()


class IncomeStatementUploadForm(forms.Form):
    ticker = forms.CharField(max_length=5, required=True, initial='TICKER')
    year = forms.DateTimeField()
    scale = forms.IntegerField(max_value=1000000)
    revenues = forms.IntegerField()
    costOfRevenues = forms.IntegerField()
    sellingGeneralAdminExpenses = forms.IntegerField()
    rAndDExpenses = forms.IntegerField()
    otherOpExpenses = forms.IntegerField()
    interestExpense = forms.IntegerField()
    interestIncome = forms.IntegerField()
    dividentPerShare = forms.IntegerField()


class CashFlowUploadForm(forms.Form):
    ticker = forms.CharField(max_length=5, required=True, initial='TICKER')
    year = forms.DateTimeField()
    scale = forms.IntegerField(max_value=1000000)
    cashFromOperations = forms.IntegerField()
    cashFromInvesting = forms.IntegerField()
    shorttermDept = forms.IntegerField()
    longTermDepth = forms.IntegerField()
    shorttermDepthrepaid = forms.IntegerField()
    longTermDethrepaid = forms.IntegerField()
    repurchaseOfCommonStock = forms.IntegerField()
    dividentPaid = forms.IntegerField()
    otherFinanceActivities = forms.IntegerField()