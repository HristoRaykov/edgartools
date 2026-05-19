import pandas as pd

from dataclasses import asdict

set_identity('hristocr@gmail.com')

company = Company('FSK')

filings = company.get_filings(form=['10-K', '10-Q'])
filing = filings[0]

non_acc = extract_nonaccrual(filing)
investments = non_acc.investments
df = pd.DataFrame([asdict(inv) for inv in investments])
non_acc.nonaccrual_rate
non_acc.period
non_acc.total_portfolio_fair_value

filing_prev = filings[1]
non_acc_prev = extract_nonaccrual(filing_prev)
investments_prev = non_acc_prev.investments
df_prev = pd.DataFrame([asdict(inv) for inv in investments_prev])
non_acc_prev.nonaccrual_rate
non_acc_prev.period
non_acc_prev.total_portfolio_fair_value
