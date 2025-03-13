import logging
from app.commands import Command


class DataCommand(Command):
    def execute(self):
        items_list = ['apple', 'banana', 'cherry']
        logging.info(f'Example List: {items_list}')
        logging.info(f'Chosen item: {items_list[0]}')
        items_list.append('date')
        logging.info(f'Updated List: {items_list}')

        items_tuple = (1, 2, 3, 4)
        logging.info(f'Example Tuple: {items_tuple}')
        logging.debug(f'First item in tuple: {items_tuple[0]}')

        first_set = {1, 2, 3, 4}
        second_set = {2, 3, 4, 5}
        logging.info(f'Example Set: {first_set}')
        logging.info(f'Difference between sets: {first_set.difference(second_set)}')
        
        first_set.add(5)
        logging.info(f'Updated Set: {first_set}')
        
        state_dict = {
            'CA': 'California',
            'NJ': 'New Jersey',
            'TX': 'Texas',
            'FL': 'Florida',
            'IL': 'Illinois'
        }
        
        logging.info(f'Example Dictionary: {state_dict}')
        state_dict['NY'] = 'New York'
        logging.info(f'Updated Dictionary: {state_dict}')
        
        for abbreviation, full_name in state_dict.items():
            logging.info(f"Abbreviation: {abbreviation} for: {full_name}")

        state_details = {
            'CA': {
                'capital': 'Sacramento',
                'population': 39538223,
                'great': 'No'
            },
            'TX': {
                'capital': 'Austin',
                'population': 29145505,
                'great': 'Yes'
            },
            'NJ': {
                'capital': 'Trenton',
                'population': 50,
                'great': 'Yes',
                'good hot dogs': 'yes',
                'where': 'Rutts hutt'
            }
        }
        
        for state, details in state_details.items():
            logging.info(f"State: {state}")
            print(f"State: {state}")
        
            for property_name, property_value in details.items():
                property_info = f"    {property_name.capitalize()}: {property_value}"
                print(property_info)
                logging.info(property_info)

