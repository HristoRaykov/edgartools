import pandas as pd

set_identity('hristocr@gmail.com')

company = Company('DXYZ')

filings = company.get_filings(form=['N-PORT', 'NPORT-P'])

# filings_df = filings.to_pandas()

report = filings[0].obj()

investment_data = report.investment_data(include_derivatives=True)

# securities_data = report.securities_data()
derivatives_data = report.derivatives_data()
futures_data = report.futures_data()
forwards_data = report.forwards_data()
options_data = report.options_data()
swaps_data = report.swaps_data()
swaptions_data = report.swaptions_data()