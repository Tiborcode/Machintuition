


class BalanceSheet:
    companyList = {}
    def __init__(self, ticker, year, scale, cashAndShortTermInv, receivables, inventory, totalCurrentAsset,
                 netPropertyPlantEquipm,
                 totalAssets, currentLiabilities, longTermLiabilities, commonEquity, totalEquity):
        self.ticker = ticker
        self.year = year
        self.scale = scale
        self.cashAndShortTermInv = cashAndShortTermInv
        self.receivables = receivables
        self.inventory = inventory
        self.calculatedTotalCurrentAssets = self.cashAndShortTermInv + self.receivables + self.inventory
        self.totalCurrentAssets = totalCurrentAsset
        self.netPropertyPlantEquipm = netPropertyPlantEquipm
        self.totalAssets = totalAssets
        self.currentLiabilities = currentLiabilities
        self.longTermLiabilities = longTermLiabilities
        self.commonEquity = commonEquity
        self.totalEquity = totalEquity
        BalanceSheet.companyList[self.ticker] = self.year

    def __str__(self):
        return f'balance sheet {self.ticker} of year {self.year} values in {self.scale}'


class IncomeStatement:
    companyList = {}

    def __init__(self, ticker, year, scale, revenues, costOfRevenues, sellingGeneralAdminExpenses, rAndDExpenses,
                 otherOpExpenses, interestExpense, interestIncome, dividentPerShare):
        self.ticker = ticker
        self.year = year
        self.scale = scale
        self.revenues = revenues
        self.costOfRevenues = costOfRevenues
        self.grossProfit = self.revenues - self.costOfRevenues
        self.sellingGeneralAdminExpenses = sellingGeneralAdminExpenses
        self.rAndDExpenses = rAndDExpenses
        self.otherOpExpenses = otherOpExpenses
        self.operatingIncome = self.grossProfit - self.sellingGeneralAdminExpenses - self.rAndDExpenses - self.otherOpExpenses
        self.interestExpense = interestExpense
        self.interestIncome = interestIncome
        self.netIncome = self.operatingIncome + self.interestIncome + self.interestExpense
        self.dividentPerShare = dividentPerShare
        IncomeStatement.companyList[self.ticker] = self.year

    def __str__(self):
        return f'income statement {self.ticker} of year {self.year} values in {self.scale}'


class CashFlow:
    companyList = {}

    def __init__(self, ticker, year, scale, cashFromOperations, cashFromInvesting, shorttermDept, longTermDepth,
                 shorttermDepthrepaid,
                 longTermDethrepaid, repurchaseOfCommonStock, dividentPaid, otherFinanceActivities):
        self.ticker = ticker
        self.year = year
        self.scale = scale
        self.cashFromOpearations = cashFromOperations
        self.cashFromInvesting = cashFromInvesting
        self.shorttermDept = shorttermDept
        self.longTermDepth = longTermDepth
        self.totalDepth = self.shorttermDept + self.longTermDepth
        self.shorttermDepthrepaid = shorttermDepthrepaid
        self.longTermDethrepaid = longTermDethrepaid
        self.totalDepthRepaid = self.shorttermDepthrepaid + self.longTermDethrepaid
        self.repurchaseOfCommonStock = repurchaseOfCommonStock
        self.dividentPaid = dividentPaid
        self.otherFinanceActivities = otherFinanceActivities
        self.cashFromFinancing = self.totalDepth + self.totalDepthRepaid + self.repurchaseOfCommonStock + self.dividentPaid + self.otherFinanceActivities
        CashFlow.companyList[self.ticker] = self.year

    def __str__(self):
        return f'cashflow {self.ticker} of year {self.year} values in {self.scale}'


# Create your models here.
