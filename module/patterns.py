import json
import os


class PatternLoader:
    """Class to handle loading pattern files."""
    
    def __init__(self, patterns_dir="patterns"):
        self.patterns_dir = patterns_dir

    def list_patterns(self):
        """List all available pattern files."""
        try:
            return [
                f.replace(".json", "") 
                for f in os.listdir(self.patterns_dir) 
                if f.endswith(".json")
            ]
        except FileNotFoundError:
            print(f"[!] Pattern directory '{self.patterns_dir}' not found.")
            return []

    def load_pattern(self, pattern_name):
        """Load a specific pattern by name."""
        pattern_file = os.path.join(self.patterns_dir, f"{pattern_name}.json")
        try:
            with open(pattern_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[!] Pattern file '{pattern_file}' not found.")
            return {}
        except json.JSONDecodeError:
            print(f"[!] Failed to parse JSON file '{pattern_file}'.")
            return {}