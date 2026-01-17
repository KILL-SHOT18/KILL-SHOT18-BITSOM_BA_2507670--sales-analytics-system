# utils/api_handler.py

def fetch_product_info(product_id: str) -> dict:
    """
    Simulates fetching real-time product information from an external API.
    Since we don't have a real API, this returns mock data for given product IDs.
    
    Args:
        product_id (str): Product ID like 'P101', 'P102', etc.
    
    Returns:
        dict: Product details containing 'name' and 'category'.
    """
    mock_product_db = {
        "P101": {"name": "Laptop Premium", "category": "Electronics"},
        "P102": {"name": "Mouse", "category": "Accessories"},
        "P103": {"name": "Keyboard", "category": "Accessories"},
        "P104": {"name": "Monitor", "category": "Electronics"},
        "P105": {"name": "Webcam", "category": "Accessories"},
        "P106": {"name": "Headphones", "category": "Audio"},
        "P107": {"name": "USB Cable", "category": "Accessories"},
        "P108": {"name": "External Hard Drive", "category": "Storage"},
        "P109": {"name": "Wireless Mouse", "category": "Accessories"},
        "P110": {"name": "Laptop Charger", "category": "Electronics"},
    }
    
    return mock_product_db.get(product_id, {"name": "Unknown Product", "category": "Unknown"})
