from dataclasses import asdict

import pandas as pd
from edgar import *
from edgar.ttm import TTMCalculator

set_identity('hristocr@gmail.com')

company = Company('GAIN')

facts = company.get_facts()

concept_facts = facts.query().by_concept('us-gaap:InvestmentCompanyDividendDistribution', exact=True).execute()
concept_facts_df = pd.DataFrame([asdict(f) for f in concept_facts])

calculator = TTMCalculator(concept_facts)
qrt = calculator.quarterize()
qrt_df = pd.DataFrame([asdict(f) for f in qrt])
print(qrt[-1].numeric_value)

# todo check TSLX Q4 us-gaap:InvestmentCompanyDividendDistribution