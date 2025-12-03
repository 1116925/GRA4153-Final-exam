'''
Performs the necessary ETL and stages the data into a appropriate object
'''
import pandas as pd

class Data:
    def __init__(self, target_CSV: str):
        self._raw_data = pd.read_csv(target_CSV)

        # Ensure observation_date is datetime
        self._raw_data['observation_date'] = pd.to_datetime(self._raw_data['observation_date'])
        self._raw_data.set_index('observation_date', inplace=True)
        self._sample = self._raw_data
        
    def set_sample_range(self, start_date: str, end_date: str):
        '''
        A setter method for the sample attribute that filters the raw data based on a date range.
        
        :param start_date: The start date for filtering
        :type start_date: str
        :param end_date: The end date for filtering
        :type end_date: str
        '''
        self._sample = self._raw_data.loc[start_date:end_date]
        
    @property
    def sample(self):
        return self._sample