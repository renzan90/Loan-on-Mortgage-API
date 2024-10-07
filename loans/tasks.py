from mortgage.celery import app
from loans.models import Loans
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from celery import shared_task


@shared_task
def calculate_eligibility(property, other_property, property_valuation, taxable_income, loan):
    one_year_from_today = date.today()+relativedelta(years=1)
    two_years_from_today = date.today()+relativedelta(years=2)
    four_years_from_today = date.today()+relativedelta(years=4)

    eligible = None

    property_valuation_condition=lambda percentage: (percentage/100)*loan.amount
    taxable_income_condition=lambda percentage: (percentage/100)*loan.amount

    if isinstance(loan, Loans):
        if property != '' or other_property != '':
            if (loan.interest>=5 and loan.interest<=6.5) \
            and (loan.return_date>=one_year_from_today \
            and loan.return_date<=two_years_from_today):
                
                if property_valuation >= property_valuation_condition(80) and \
                taxable_income >= taxable_income_condition(20):
                    eligible = True
                else:
                    eligible = False
            
                return eligible
                
            elif (loan.interest>=6 and loan.interest<=8) \
            and (loan.return_date>=one_year_from_today \
            and loan.return_date<=four_years_from_today):
                
                ideal_property_valuation1 = int(property_valuation_condition(85))
                ideal_property_valuation2 = int(property_valuation_condition(90))

                ideal_taxable_income1 = int(taxable_income_condition(25))
                ideal_taxable_income2 = int(taxable_income_condition(30))
                
                if property_valuation in range(ideal_property_valuation1, ideal_property_valuation2+1)\
                and taxable_income in range(ideal_taxable_income1, ideal_taxable_income2+1):
                    eligible = True
                else:
                    eligible = False
                
            elif (loan.interest>=8 and loan.interest<=10) \
            and (loan.return_date<four_years_from_today):
                
                ideal_property_valuation = int(property_valuation_condition(90))

                ideal_taxable_income1 = int(taxable_income_condition(30))
                ideal_taxable_income2 = int(taxable_income_condition(40))
                
                if property_valuation >= ideal_property_valuation\
                and taxable_income in range(ideal_taxable_income1, ideal_taxable_income2+1):
                    eligible = True
                else:
                    eligible = False
        
    return eligible