"""
Main Application Runner - Indian Formula Racing Investment Strategies.
Bridges ingestion and analysis modules to highlight F1 corporate sponsorship values.

Author: Student Employee
Course: Vibe Code Project - Phase 2 & Phase 3
"""
from data_loader import parse_csv_string
from analytics import aggregate_financials_by_role, compute_group_averages


# ==============================================================================
# PHASE 3 ADDITIONS: Preconditions, Custom Key Sorting, Linear & Binary Search
# ==============================================================================

def get_role_cost_key(role_item: tuple) -> float:
    """
    Phase 3 Custom Sort Key Function: Extracts 'avg_cost' from a (role, stats) tuple.
    """
    assert isinstance(role_item, tuple) and len(role_item) == 2, (
        "Precondition failed: role_item must be a (role, stats) tuple."
    )
    return role_item[1]['avg_cost']


def get_record_cost_key(row_record: dict) -> float:
    """
    Phase 3 Custom Sort Key Function: Extracts Investment_Millions_USD as a float.
    """
    assert isinstance(row_record, dict) and 'Investment_Millions_USD' in row_record, (
        "Precondition failed: row_record must contain 'Investment_Millions_USD'."
    )
    return float(row_record['Investment_Millions_USD'])


def sort_records_by_cost(records_list: list, descending: bool = False) -> list:
    """
    Phase 3 Custom Key Sorting: Sorts dataset records by cost using get_record_cost_key.
    """
    assert isinstance(records_list, list) and len(records_list) > 0, (
        "Precondition failed: records_list must be a non-empty list."
    )
    assert isinstance(descending, bool), "Precondition failed: descending must be a boolean."
    return sorted(records_list, key=get_record_cost_key, reverse=descending)


def linear_search_by_role(records_list: list, target_role: str) -> list:
    """
    Phase 3 Linear Search: Scans records sequentially to find all rows matching target_role.
    """
    assert isinstance(records_list, list) and len(records_list) > 0, (
        "Precondition failed: records_list must be a non-empty list."
    )
    assert isinstance(target_role, str) and len(target_role.strip()) > 0, (
        "Precondition failed: target_role must be a non-empty string."
    )
    matches = []
    for row in records_list:
        if row['Involvement_Role'] == target_role:
            matches.append(row)
    return matches


def binary_search_by_cost(sorted_records: list, target_cost: float) -> int:
    """
    Phase 3 Binary Search: Searches a cost-sorted record list for target_cost.
    """
    assert isinstance(sorted_records, list) and len(sorted_records) > 0, (
        "Precondition failed: sorted_records must be a non-empty list."
    )
    assert isinstance(target_cost, (int, float)) and target_cost >= 0, (
        "Precondition failed: target_cost must be a non-negative number."
    )
    assert all(
        get_record_cost_key(sorted_records[i]) <= get_record_cost_key(sorted_records[i + 1])
        for i in range(len(sorted_records) - 1)
    ), "Precondition failed: sorted_records must be sorted in ascending order."

    low = 0
    high = len(sorted_records) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_cost = get_record_cost_key(sorted_records[mid])

        if mid_cost == float(target_cost):
            return mid
        elif mid_cost < float(target_cost):
            low = mid + 1
        else:
            high = mid - 1

    return -1


# ==============================================================================
# PHASE 2 CODE (KEPT INTACT) + PHASE 3 PRECONDITIONS & CUSTOM SORT
# ==============================================================================

def print_performance_dashboard(summary_averages: dict):
    """
    Renders structured calculation reports cleanly onto the terminal display.
    Fulfills the Single Responsibility Principle by managing display formatting only.

    Args:
        summary_averages (dict): Statistical metrics grouped by corporate strategy.
    """
    # Phase 3 Precondition
    assert isinstance(summary_averages, dict) and len(summary_averages) > 0, (
        "Precondition failed: summary_averages must be a non-empty dictionary."
    )

    print("=" * 70)
    print(f"{'WHY INDIAN COMPANIES PREFER SPONSORSHIP OVER OWNERSHIP':^70}")
    print("=" * 70)
    print(f"{'Strategic Corporate Role':<25} | {'Avg Cost ($M)':<14} | {'Avg Profit ($M)':<14} | {'Avg ROI %':<10}")
    print("-" * 70)
    
    # Phase 3 Custom Key Sort (keeps Team Owner first, Title Sponsor second)
    sorted_summary = sorted(summary_averages.items(), key=get_role_cost_key, reverse=True)

    for role, stats in sorted_summary:
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

    # Step 5 (Phase 3): Execute Linear Search, Custom Key Sorting, and Binary Search
    sponsor_records = linear_search_by_role(raw_records, "Title Sponsor")
    cost_sorted_records = sort_records_by_cost(raw_records, descending=False)
    found_index = binary_search_by_cost(cost_sorted_records, 15.0)
    assert len(sponsor_records) > 0 and found_index != -1, "Phase 3 search verification passed."


if __name__ == '__main__':
    main()