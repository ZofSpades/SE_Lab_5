"""
Inventory Management System

A simple inventory system for managing stock items with add, remove,
load, save, and reporting functionality.
"""
import json
from datetime import datetime


class InventoryManager:
    """Manages inventory stock data."""

    def __init__(self):
        """Initialize inventory with empty stock data."""
        self.stock_data = {}

    def add_item(self, item="default", qty=0, logs=None):
        """Add an item to the inventory with optional logging."""
        if logs is None:
            logs = []
        if not item:
            return
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        logs.append(f"{datetime.now()}: Added {qty} of {item}")

    def remove_item(self, item, qty):
        """Remove a specified quantity of an item from inventory."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            print(f"Warning: Item '{item}' not found in inventory")

    def get_qty(self, item):
        """Get the quantity of an item in inventory."""
        return self.stock_data.get(item, 0)

    def load_data(self, file="inventory.json"):
        """Load inventory data from a JSON file."""
        try:
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.loads(f.read())
        except FileNotFoundError:
            print(f"Warning: File '{file}' not found. "
                  f"Starting with empty inventory.")

    def save_data(self, file="inventory.json"):
        """Save inventory data to a JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            f.write(json.dumps(self.stock_data))

    def print_data(self):
        """Print current inventory report."""
        print("Items Report")
        for item in self.stock_data:
            print(item, "->", self.stock_data[item])

    def check_low_items(self, threshold=5):
        """Check for items with quantity below threshold."""
        result = []
        for item in self.stock_data:
            if self.stock_data[item] < threshold:
                result.append(item)
        return result


def main():
    """Main function to demonstrate inventory operations."""
    inventory = InventoryManager()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", -2)
    # Type validation removed - should validate inputs in production
    print("Warning: Invalid type inputs should be validated")
    inventory.remove_item("apple", 3)
    inventory.remove_item("orange", 1)
    print("Apple stock:", inventory.get_qty("apple"))
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()
    # Removed dangerous eval() - using safe alternative
    print('Safe print instead of eval')


main()
