"""
Main Application Runner - Indian Formula Racing Investment Strategies.
Bridges ingestion and analysis modules to highlight F1 corporate sponsorship values.

Author: Student Employee
Course: Vibe Code Project - Phase 2
"""
from data_loader import parse_csv_string
from analytics import aggregate_financials_by_role, compute_group_averages

def print_performance_dashboard(summary_averages: dict):
    """
    Renders structured calculation reports cleanly onto the terminal display.
    Fulfills the Single Responsibility Principle by managing display formatting only.

    Args:
        summary_averages (dict): Statistical metrics grouped by corporate strategy.
    """
    print("=" * 70)
    print(f"{'WHY INDIAN COMPANIES PREFER SPONSORSHIP OVER OWNERSHIP':^70}")
    print("=" * 70)
    print(f"{'Strategic Corporate Role':<25} | {'Avg Cost ($M)':<14} | {'Avg Profit ($M)':<14} | {'Avg ROI %':<10}")
    print("-" * 70)
    
    for role, stats in summary_averages.items():
        print(f"{role:<25} | "
              f"{stats['avg_cost']:<14.2f} | "
              f"{stats['avg_profit']:<14.2f} | "
              f"{stats['avg_roi']:<10.1f}%")
    print("=" * 70)

def main():
    """
    Orchestrates system functions to process racing metrics data workflows.
    Ensures clear separation of data propagation between modules.
    """
    csv_data = """Year,Indian_Company_Entity,Involvement_Role,Racing_Series,Racer_Name,Races_Entered,Podiums_Achieved,Races_Won,Win_Rate_Percentage,Investment_Millions_USD,Net_Profit_Loss_Millions_USD,ROI_Percentage,Host_Track_Context
2008,Force India,Team Owner,Formula 1,Adrian Sutil,18,0,0,0,120,-25,-20.8,International
2008,Force India,Team Owner,Formula 1,Giancarlo Fisichella,18,0,0,0,120,-25,-20.8,International
2009,Force India,Team Owner,Formula 1,Giancarlo Fisichella,12,1,0,0,130,-15,-11.5,International
2009,Force India,Team Owner,Formula 1,Adrian Sutil,17,0,0,0,130,-15,-11.5,International
2009,Force India,Team Owner,Formula 1,Vitantonio Liuzzi,5,0,0,0,130,-15,-11.5,International
2010,Force India,Team Owner,Formula 1,Adrian Sutil,19,0,0,0,140,-5,-3.6,International
2010,Force India,Team Owner,Formula 1,Vitantonio Liuzzi,19,0,0,0,140,-5,-3.6,International
2011,Force India,Team Owner,Formula 1,Adrian Sutil,19,0,0,0,145,2,1.4,Buddh Int. Circuit
2011,Force India,Team Owner,Formula 1,Paul di Resta,19,0,0,0,145,2,1.4,Buddh Int. Circuit
2012,Force India,Team Owner,Formula 1,Nico HÃ¼lkenberg,20,0,0,0,150,4,2.7,Buddh Int. Circuit
2012,Force India,Team Owner,Formula 1,Paul di Resta,20,0,0,0,150,4,2.7,Buddh Int. Circuit
2013,Force India,Team Owner,Formula 1,Adrian Sutil,19,0,0,0,152,5,3.3,Buddh Int. Circuit
2013,Force India,Team Owner,Formula 1,Paul di Resta,19,0,0,0,152,5,3.3,Buddh Int. Circuit
2014,Force India,Team Owner,Formula 1,Nico HÃ¼lkenberg,19,0,0,0,160,8,5,International
2014,Force India,Team Owner,Formula 1,Sergio PÃ©rez,19,1,0,0,160,8,5,International
2015,Force India,Team Owner,Formula 1,Nico HÃ¼lkenberg,19,0,0,0,165,10,6.1,International
2015,Force India,Team Owner,Formula 1,Sergio PÃ©rez,19,1,0,0,165,10,6.1,International
2016,Force India,Team Owner,Formula 1,Nico HÃ¼lkenberg,21,0,0,0,175,15,8.6,International
2016,Force India,Team Owner,Formula 1,Sergio PÃ©rez,21,2,0,0,175,15,8.6,International
2017,Force India,Team Owner,Formula 1,Sergio PÃ©rez,20,0,0,0,190,-12,-6.3,International
2017,Force India,Team Owner,Formula 1,Esteban Ocon,20,0,0,0,190,-12,-6.3,International
2018,Force India,Team Owner,Formula 1,Sergio PÃ©rez,12,1,0,0,110,-35,-31.8,International
2018,Force India,Team Owner,Formula 1,Esteban Ocon,12,0,0,0,110,-35,-31.8,International
2014-15,Mahindra Racing,Team Owner,Formula E,Karun Chandhok,11,0,0,0,15,-2.5,-16.7,International
2014-15,Mahindra Racing,Team Owner,Formula E,Bruno Senna,11,0,0,0,15,-2.5,-16.7,International
2015-16,Mahindra Racing,Team Owner,Formula E,Nick Heidfeld,10,1,0,0,18,-1,-5.6,International
2015-16,Mahindra Racing,Team Owner,Formula E,Bruno Senna,10,0,0,0,18,-1,-5.6,International
2016-17,Mahindra Racing,Team Owner,Formula E,Felix Rosenqvist,12,5,1,8.3,22,1.5,6.8,International
2016-17,Mahindra Racing,Team Owner,Formula E,Nick Heidfeld,12,5,0,0,22,1.5,6.8,International
2017-18,Mahindra Racing,Team Owner,Formula E,Felix Rosenqvist,12,2,2,16.7,25,3,12,International
2017-18,Mahindra Racing,Team Owner,Formula E,Nick Heidfeld,12,0,0,0,25,3,12,International
2018-19,Mahindra Racing,Team Owner,Formula E,JÃ©rÃ´me d'Ambrosio,13,2,1,7.7,28,2,7.1,International
2018-19,Mahindra Racing,Team Owner,Formula E,Pascal Wehrlein,12,1,0,0,28,2,7.1,International
2019-20,Mahindra Racing,Team Owner,Formula E,JÃ©rÃ´me d'Ambrosio,11,0,0,0,30,-0.5,-1.7,International
2019-20,Mahindra Racing,Team Owner,Formula E,Pascal Wehrlein,5,0,0,0,30,-0.5,-1.7,International
2020-21,Mahindra Racing,Team Owner,Formula E,Alexander Sims,15,1,0,0,32,0.8,2.5,International
2020-21,Mahindra Racing,Team Owner,Formula E,Alex Lynn,15,3,1,6.7,32,0.8,2.5,International
2021-22,Mahindra Racing,Team Owner,Formula E,Oliver Rowland,16,1,0,0,35,-1.2,-3.4,International
2021-22,Mahindra Racing,Team Owner,Formula E,Alexander Sims,16,1,0,0,35,-1.2,-3.4,International
2022-23,Mahindra Racing,Team Owner,Formula E,Lucas di Grassi,16,1,0,0,40,4.5,11.2,Hyderabad Street Circuit
2022-23,Mahindra Racing,Team Owner,Formula E,Oliver Rowland,9,0,0,0,40,4.5,11.2,Hyderabad Street Circuit
2023-24,Mahindra Racing,Team Owner,Formula E,Nyck de Vries,14,0,0,0,42,-2,-4.8,International
2023-24,Mahindra Racing,Team Owner,Formula E,Edoardo Mortara,16,0,0,0,42,-2,-4.8,International
2024-25,Mahindra Racing,Team Owner,Formula E,Nyck de Vries,16,0,0,0,45,-3.5,-7.8,International
2024-25,Mahindra Racing,Team Owner,Formula E,Edoardo Mortara,16,1,0,0,45,-3.5,-7.8,International
2025-26,Mahindra Racing,Team Owner,Formula E,Nyck de Vries,16,1,0,0,48,-1,-2.1,International
2005,Tata Group,Title Sponsor,Formula 1,Narain Karthikeyan,19,0,0,0,15,3.5,23.3,International
2010,Tata Group,Title Sponsor,Formula 1,Karun Chandhok,10,0,0,0,10,1.2,12,International
2011,Jaypee Group,Title Sponsor,Formula 1,Narain Karthikeyan,9,0,0,0,12,-2,-16.7,Buddh Int. Circuit
2012,Tata Group,Title Sponsor,Formula 1,Narain Karthikeyan,20,0,0,0,8,0.5,6.3,Buddh Int. Circuit
2014,MRF Tyres,Title Sponsor,Formula 3,Tarun Reddy,12,4,2,16.7,1.5,0.3,20,Buddh Int. Circuit
2015,MRF Tyres,Title Sponsor,Formula 3,Tarun Reddy,14,6,3,21.4,1.8,0.4,22.2,Buddh Int. Circuit
2016,JK Tyre,Title Sponsor,Formula BMW,Ananth Shanmugam,10,3,1,10,1.2,0.1,8.3,Buddh Int. Circuit"""

    # Step 1: Parse data via the ingestion module
    raw_records = parse_csv_string(csv_data)
    
    # Step 2: Apply grouping transformations to structured dictionary objects
    grouped_map = aggregate_financials_by_role(raw_records)
    
    # Step 3: Compute final math statistics
    final_averages = compute_group_averages(grouped_map)
    
    # Step 4: Render final console table to user screen
    print_performance_dashboard(final_averages)

if __name__ == '__main__':
    main()
