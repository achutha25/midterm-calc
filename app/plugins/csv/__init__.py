import logging
import os
from app.commands import Command
import pandas as pd


class CsvCommand(Command):
    def execute(self):
        directory = './data'
        if not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created directory: {directory}")

        elif not os.access(directory, os.W_OK):
            logging.error(f"Directory {directory} is not writable.")
            return
        
        state_dict = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois',
            'NY': 'New York'
        }
        df = pd.DataFrame(list(state_dict.items()), columns=['Abbreviation', 'State'])
        file_path = os.path.join(directory, 'states.csv')
        df.to_csv(file_path, index=False)
        
        logging.info(f"CSV saved at: {file_path}")
        
        new_file_path = os.path.join(directory, 'gpt_states.csv')
        logging.info(f"Relative path for saving: {new_file_path}")
        
        absolute_file_path = os.path.abspath(new_file_path)
        logging.info(f"Absolute path for saving: {absolute_file_path}")
        
        df_loaded = pd.read_csv(new_file_path)
        
        print("States from CSV:")
        for idx, row in df_loaded.iterrows():
            state_info = f"{row['State Abbreviation']}: {row['State Name']}"
            print(f"Record {idx}: {state_info}")
            logging.info(f"Record {idx}: {state_info}")
            
            for field in row.index:
                field_details = f"    {field}: {row[field]}"
                print(field_details)
                logging.info(f"Index: {idx}, {field_details}")

