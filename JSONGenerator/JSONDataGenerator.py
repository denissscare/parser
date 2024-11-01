from typing import Any, Dict, List
import json

class JSONDataGenerator:
    def __init__(self):
        self.json = []
    
    def add_item(self,
                 item: Dict[str, Any]) -> None:
        self.json.append(item)
        
            
    def generate_json(self,
                      indent: int = 4) -> str:
        return json.dumps(self.json, indent=indent, ensure_ascii=False)
    
    def save_to_file(self,
                     file_path: str,
                     indent: int = 4) -> None:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.json, file, indent=indent, ensure_ascii=False)