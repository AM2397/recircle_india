# This Management Command could be used to load the Waste Recovery Data into StateStats Table
from django.core.management.base import BaseCommand
from recircle_app.models import StateStats
import pandas as pd


class Command(BaseCommand):
    help = 'Update State Wise Waste Recovery Data'

    @staticmethod
    def update_state_wise_statistics(data_path):
        df = pd.read_excel(data_path, sheet_name='Sheet1')  # Read Excel File Data using Pandas
        for index, row in df.iterrows():
            # Iterating Dataframe and retrieving every column data
            state_code = row['state_code']
            state_name = row['state_name']
            rigid = row['rigid']
            flexible = row['flexible']
            mlp = row['mlp']

            # Check if the field value is either missing or null value exists
            if pd.isna(state_code) or pd.isna(state_name) or pd.isna(rigid) or pd.isna(flexible) or pd.isna(mlp):
                continue

            state_code = str(state_code).strip()
            state_name = str(state_name).strip()

            # Check if value is as per mathematical format then replace the ',' from the Number
            # Example: 10,000 -> 10000

            rigid = str(rigid).replace(',', '')
            flexible = str(flexible).replace(',', '')
            mlp = str(mlp).replace(',', '')

            # Create StateStats Object and load into Table
            state_object = StateStats(
                state_code=state_code,
                state_name=state_name,
                rigid=rigid,
                flexible=flexible,
                mlp=mlp
            )
            state_object.save()

    def handle(self, *args, **kwargs):
        # Physical path to Excel File
        data_path = 'stats_data/state_wise_stats_data.xlsx'
        try:
            self.update_state_wise_statistics(data_path)
            print("State Wise State Recovery Stats Data Uploaded Successfully!!")
        except RuntimeError:
            print("Exception Occurred")
