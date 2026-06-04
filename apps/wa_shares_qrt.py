from dataclasses import asdict

import pandas as pd

from edgar import Company, set_identity
from edgar.ttm import TTMCalculator, DurationBucket

set_identity('hristocr@gmail.com')

company = Company('FSK')

facts = company.get_facts()
facts_df = pd.DataFrame([asdict(f) for f in facts])

shares_facts = facts.query().by_concept(f'us-gaap:WeightedAverageNumberOfSharesOutstandingBasic', exact=True).execute()
shares_facts_df = pd.DataFrame([asdict(f) for f in shares_facts])

shares_calculator = TTMCalculator(shares_facts)
fy_shares_list = shares_calculator._filter_by_duration(DurationBucket.ANNUAL)
ytd9_shares_list = shares_calculator._filter_by_duration(DurationBucket.YTD_9M)
q_shares_list = shares_calculator._filter_by_duration(DurationBucket.QUARTER)

# Build lookup by fiscal year
fy_shares_by_year = {s.fiscal_year: s.numeric_value for s in fy_shares_list}
ytd9_shares_by_year = {s.fiscal_year: s.numeric_value for s in ytd9_shares_list}

for year, fy_shares in fy_shares_by_year.items():
    ytd9_shares = ytd9_shares_by_year[year]
    q4_shares = 4 * fy_shares - 3 * ytd9_shares

# q_shares_by_year: dict = {}
# for s in q_shares_list:
#     q_shares_by_year.setdefault(s.fiscal_year, []).append(s.numeric_value)

df = pd.DataFrame([asdict(f) for f in fy_shares_list])