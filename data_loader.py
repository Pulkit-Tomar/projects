"""
Data Ingestion and Parsing Module.
Responsible exclusively for low-level stream reading and CSV string extraction.
"""
import csv

def parse_csv_string(csv_data_string: str) -> list:
    """
    Parses a multi-line raw CSV text block into a list of structured row records.

    Args:
        csv_data_string (str): The raw text string containing dataset rows.

    Returns:
        list: A sequence of dictionary rows mapping column headers to row values.
    """
    cleaned_data = csv_data_string.strip()
    lines = cleaned_data.split('\n')
    reader = csv.DictReader(lines)
    return list(reader)


