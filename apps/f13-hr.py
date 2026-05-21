from dataclasses import asdict

import numpy as np
import pandas as pd

from edgar import Company, set_identity

set_identity('hristocr@gmail.com')

# 1503174 BRK.A
company = Company('AFG')

filings = company.get_filings(form="13F-HR")
filling = filings[0]
report = filling.obj()
report.report_period
# primary_form_information = report.primary_form_information
info = report.infotable

managers = report.other_managers
df_managers = pd.DataFrame([asdict(manager) for manager in managers])
# pman = report.get_portfolio_managers()

holdings = report.holdings
# holdings_view = report.holdings_view()
# previous = report.previous_holding_report()

compare_holdings = report.compare_holdings(display_limit=500).data
history = report.holding_history(periods=4, display_limit=500).data
