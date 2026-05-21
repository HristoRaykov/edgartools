from dataclasses import asdict

import pandas as pd

from edgar import Company, set_identity
from edgar.ttm import TTMCalculator

set_identity('hristocr@gmail.com')

company = Company('AAPl')

facts = company.get_facts()
# facts_df = facts.to_dataframe()

concept = 'NetIncomeLoss'
concept_facts = facts.query().by_concept(f'us-gaap:{concept}', exact=True).execute()
concept_facts_full = pd.DataFrame([asdict(f) for f in concept_facts])
# concept_facts_df = facts.query().by_concept(f'us-gaap:{concept}', exact=True).to_dataframe()
# concept_time_series = facts.time_series(concept, periods=10000)

calculator = TTMCalculator(concept_facts)
qrt_facts = calculator.quarterize()
qrt_facts_df = pd.DataFrame([asdict(f) for f in qrt_facts])
ttm_trend = calculator.calculate_ttm_trend(periods=100)

df = qrt_facts_df[['label', 'value', 'period_start', 'period_end', ]]
df = df.sort_values('period_end')
df['ttm'] = df['value'].rolling(window=4).sum()

ttm_trend = ttm_trend.merge(df, left_on='as_of_date', right_on='period_end', how='left')
ttm_trend['diff'] = ttm_trend['ttm_value'] - ttm_trend['ttm']
