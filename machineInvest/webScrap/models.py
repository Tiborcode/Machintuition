from django import forms
from django.db import models
import uuid

class Report(forms.Form):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    ticker = models.CharField(max_length=5)
    currency = models.CharField(max_length=3, default="USD")
    year = models.PositiveIntegerField()
    fiscal_period = models.CharField(
        max_length=20,
        choices=[
            ("FY", "Full Year"),
            ("Q1", "Quarter 1"),
            ("Q2", "Quarter 2"),
            ("Q3", "Quarter 3"),
            ("Q4", "Quarter 4"),
        ],
    )
    scale = forms.IntegerField(max_value=1000000)
    metadata = models.JSONField(
        blank=True,
        default=dict,
        help_text="Optional additional attributes"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("ticker", "year", "fiscal_period")
        indexes = [
            models.Index(fields=["ticker", "year"]),]

        def __str__(self):
            return f"{self.ticker} {self.year} {self.fiscal_period}"

class BalanceSheetuploadForm(forms.Form):
    report = models.OneToOneField(
        'Report',
        on_delete=models.CASCADE,
        related_name="balance_sheet"
    )


    cashAndShortTermInv = models.IntegerField()
    receivables = models.IntegerField()
    inventory = models.IntegerField()
    calculatedTotalCurrentAssests = models.IntegerField() # calculatedTotalCurrentAssests + cashAndShortTermInv + receivables + inventory
    totalCurrentAsset = models.IntegerField()
    netPropertyPlantEquipm = models.IntegerField()
    totalAssets = models.IntegerField()
    currentLiabilities = models.IntegerField()
    longTermLiabilities = models.IntegerField()
    commonEquity = models.IntegerField()
    totalEquity = models.IntegerField()



class IncomeStatementUploadForm(forms.Form):
    report = models.OneToOneField(
        'Report',
        on_delete=models.CASCADE,
        related_name="income_statement"
    )
    revenues = models.IntegerField()
    costOfRevenues = models.IntegerField()
    grossProfit = models.IntegerField() #grossProfit = revenues + costOfRevenues
    sellingGeneralAdminExpenses = models.IntegerField()
    rAndDExpenses = models.IntegerField()
    otherOpExpenses = models.IntegerField()
    operatingIncome = models.IntegerField() # operatingIncome = grossProfit + sellingGeneralAdminExpenses + rAndDExpenses + otherOpExpenses
    interestExpense = models.IntegerField()
    interestIncome = models.IntegerField()
    netincome = models.IntegerField() # netincome = operatingIncome + interestExpense + interestIncome
    dividentPerShare = models.IntegerField()



class CashFlowUploadForm(forms.Form):
    report = models.OneToOneField(
        'Report',
        on_delete=models.CASCADE,
        related_name="cashflow"
    )
    cashFromOperations = models.IntegerField()
    cashFromInvesting = models.IntegerField()
    shorttermDept = models.IntegerField()
    longTermDepth = models.IntegerField()
    totalDepth = models.IntegerField() #totalDepth = shorttermDept + longTermDepth
    shorttermDepthrepaid = models.IntegerField()
    longTermDethrepaid = models.IntegerField()
    totalDepthRepaid = models.IntegerField() #totaldepthrepaid =shorttermDepthrepaid + longTermDethrepaid
    repurchaseOfCommonStock = models.IntegerField()
    dividentPaid = models.IntegerField()
    otherFinanceActivities = models.IntegerField()
    cashFromFinancing = models.IntegerField() #cashFromFinancing = totalDepth + totalDepthRepaid + repurchaseOfCommonStock + dividentPaid + otherFinanceActivities


class FutureAspects(forms.Form):
    report = models.OneToOneField(
        'Report',
        on_delete=models.CASCADE,
        related_name="future_aspects"
    )
    aspects = forms.CharField()
    growthAspects = forms.CharField()
    marketAspects = forms.CharField()
