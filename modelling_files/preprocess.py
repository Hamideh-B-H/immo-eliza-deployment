import pandas as pd

class Preprocessor:
    def __init__(self, postal_mean):
        self.postal_mean = postal_mean

    def transform(self, number_rooms=None, living_area=None, property_type=None, state=None, postal_code=None):
        # --- Handle missing numeric values ---
        if number_rooms is None or not isinstance(number_rooms, (int, float)):
            number_rooms = 1  # default value
        if living_area is None or not isinstance(living_area, (int, float)):
            living_area = 50  # default value

        # --- Handle missing categorical values ---
        if property_type not in ['house', 'apartment']:
            property_type = 'apartment'  # default category
        if state not in ['ready_to_move_in', 'under_construction']:
            state = 'ready_to_move_in'  # default category

        # --- Handle missing postal_code ---
        if postal_code is None:
            postal_code = '0000'  # default postal code
        postal_code = str(postal_code)

        # --- Create DataFrame ---
        df = pd.DataFrame({
            "number_rooms": [number_rooms],
            "living_area": [living_area],
            "property_type_name": [property_type],
            "state_mapped": [state],
            "postal_code": [postal_code]
        })

        # --- Encode categorical features ---
        df['property_house'] = (df['property_type_name'] == 'house').astype(int)
        df['state_ready'] = (df['state_mapped'] == 'ready_to_move_in').astype(int)

        # --- Target encoding for postal code ---
        df['postal_code_target'] = df['postal_code'].map(self.postal_mean)
        df['postal_code_target'] = df['postal_code_target'].fillna(self.postal_mean.mean())

        # --- Return model-ready features ---
        return df[['number_rooms', 'living_area', 'property_house', 'state_ready', 'postal_code_target']]
