'''
Performs the necessary ETL and stages the data into a appropriate object
'''
import pandas as pd

class Data:
    def __init__(self, target_CSV: str):
        self._raw_data = pd.read_csv(target_CSV)
        self._sample = self._raw_data

        # Ensure observation_date is datetime
        self._raw_data['observation_date'] = pd.to_datetime(self._raw_data['observation_date'])
        
    def set_sample_range(self, start_date: str, end_date: str):
        '''
        A setter method for the sample attribute that filters the raw data based on a date range.
        
        :param start_date: The start date for filtering
        :type start_date: str
        :param end_date: The end date for filtering
        :type end_date: str
        '''
        mask = (self._raw_data['observation_date'] >= start_date) & (self._raw_data['observation_date'] <= end_date)
        self._sample = self._raw_data.loc[mask] 
        
    @property
    def sample(self):
        return self._sample