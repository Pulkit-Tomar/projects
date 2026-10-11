"""
Business Intelligence and Financial Analytics Engine.
Processes structured racing dataset inputs to extract and aggregate performance metrics.
"""

def extract_financial_values(row_record: dict) -> dict:
    """
    Safely converts string column records into structured float values.
    Refactors repeated type-casting logic into a single definition point.

    Args:
        row_record (dict): A single row dictionary data entry.

    Returns:
        dict: Standardized dictionary containing cast float values for cost, profit, and ROI.
    """
    return {
        'cost': float(row_record['Investment_Millions_USD']),
        'profit': float(row_record['Net_Profit_Loss_Millions_USD']),
        'roi': float(row_record['ROI_Percentage'])
    }

def aggregate_financials_by_role(records_list: list) -> dict:
    """
    Groups raw financial metric lists inside a dictionary organized by corporate role.

    Args:
        records_list (list): List of row dictionary objects from the data loader.

    Returns:
        dict: A refined dictionary data structure grouping float sequences by involvement keys.
    """
    role_groupings = {}
    
    for row in records_list:
        role = row['Involvement_Role']
        financials = extract_financial_values(row)
        
        if role not in role_groupings:
            role_groupings[role] = {'costs': [], 'profits': [], 'rois': []}
            
        role_groupings[role]['costs'].append(financials['cost'])
        role_groupings[role]['profits'].append(financials['profit'])
        role_groupings[role]['rois'].append(financials['roi'])
        
    return role_groupings

def compute_group_averages(grouped_data: dict) -> dict:
    """
    Computes mathematical averages across aggregated investment dictionary matrices.

    Args:
        grouped_data (dict): Categorized numerical sequences structured by corporate role.

    Returns:
        dict: Summary metrics mapping calculated average variables back to unique role keys.
    """
    calculated_summaries = {}
    
    for role, metrics in grouped_data.items():
        calculated_summaries[role] = {
            'avg_cost': sum(metrics['costs']) / len(metrics['costs']),
            'avg_profit': sum(metrics['profits']) / len(metrics['profits']),
            'avg_roi': sum(metrics['rois']) / len(metrics['rois'])
        }
        
    return calculated_summaries

