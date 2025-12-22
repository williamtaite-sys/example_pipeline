"""
Data Processor Module
=====================

This module provides utilities for cleaning and validating pipeline data.
"""

def clean_record(record):
    """
    Cleans a single data record by removing leading/trailing whitespace 
    from string values and converting keys to lowercase.

    Args:
        record (dict): The raw data record to clean.

    Returns:
        dict: The cleaned record.
    """
    return {k.lower(): (v.strip() if isinstance(v, str) else v) for k, v in record.items()}

def validate_data(data_list, required_fields):
    """
    Checks if all records in a list contain the required fields.

    Args:
        data_list (list): A list of dictionaries representing records.
        required_fields (list): A list of field names that must be present.

    Returns:
        tuple: (bool, list) - Success status and a list of error messages.
    """
    errors = []
    for i, record in enumerate(data_list):
        for field in required_fields:
            if field not in record:
                errors.append(f"Record {i} is missing required field: {field}")
    
    return len(errors) == 0, errors
