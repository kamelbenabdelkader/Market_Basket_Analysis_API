
from typing import Optional, Union
from pydantic import BaseModel
import joblib


class Test(BaseModel):
    id: Optional[int]
    FL_DATE : Optional[str]
    AIRLINE_ID : Optional[int]
    ORIGIN_AIRPORT_ID : Optional[int]
    DEST_AIRPORT_ID : Optional[int]
    DEP_TIME: Optional[str]

class Data(BaseModel):
    id: Optional[int]
    QUARTER : Optional[int]
    MONTH : Optional[int]
    DAY_OF_MONTH : Optional[int]
    DAY_OF_WEEK: Optional[int]
    ORIGIN_AIRPORT_ID : Optional[int]
    DEST_AIRPORT_ID : Optional[int]
    DEP_TIME: Optional[str]
    ARR_TIME: Optional[str]
    VACATION : Optional[int]


class Predict(BaseModel):
    id: Optional[int]
    TARGET : Optional[int]
    PROB : Optional[int]


class TableBdd(BaseModel):
    YEAR: Optional[int]
    QUARTER: Optional[int]
    MONTH: Optional[int]
    DAY_OF_MONTH: Optional[int]
    DAY_OF_WEEK: Optional[int]
    FL_DATE: Optional[str]
    UNIQUE_CARRIER: Optional[str]
    AIRLINE_ID: Optional[int]
    CARRIER: Optional[str]
    TAIL_NUM: Optional[str]
    FL_NUM: Optional[int]
    ORIGIN_AIRPORT_ID: Optional[int]
    ORIGIN_AIRPORT_SEQ_ID: Optional[int]
    ORIGIN_CITY_MARKET_ID: Optional[int]
    ORIGIN: Optional[str]
    ORIGIN_CITY_NAME: Optional[str]
    ORIGIN_STATE_ABR: Optional[str]
    ORIGIN_STATE_FIPS: Optional[int]
    ORIGIN_STATE_NM: Optional[str]
    ORIGIN_WAC: Optional[int]
    DEST_AIRPORT_ID: Optional[int]
    DEST_AIRPORT_SEQ_ID: Optional[int]
    DEST_CITY_MARKET_ID: Optional[int]
    DEST: Optional[str]
    DEST_CITY_NAME: Optional[str]
    DEST_STATE_ABR: Optional[str]
    DEST_STATE_FIPS: Optional[int]
    DEST_STATE_NM: Optional[str]
    DEST_WAC: Optional[int]
    CRS_DEP_TIME: Optional[int]
    DEP_TIME: Optional[int]
    DEP_DELAY: Union[float, None]
    DEP_DELAY_NEW: Union[float, None]
    DEP_DEL15: Union[float, None]
    DEP_DELAY_GROUP: Optional[int]
    DEP_TIME_BLK: Optional[str]
    TAXI_OUT: Union[float, None]
    WHEELS_OFF: Optional[int]
    WHEELS_ON: Optional[int]
    TAXI_IN: Union[float, None]
    CRS_ARR_TIME: Optional[int]
    ARR_TIME: Optional[int]
    ARR_DELAY: Union[float, None]
    ARR_DELAY_NEW: Union[float, None]
    ARR_DEL15: Union[float, None]
    ARR_DELAY_GROUP: Optional[int]
    ARR_TIME_BLK: Optional[str]
    CANCELLED: Union[float, None]
    CANCELLATION_CODE: Optional[str]
    DIVERTED: Union[float, None]
    CRS_ELAPSED_TIME: Union[float, None]
    ACTUAL_ELAPSED_TIME: Union[float, None]
    AIR_TIME: Union[float, None]
    FLIGHTS: Union[float, None]
    DISTANCE: Union[float, None]
    DISTANCE_GROUP: Optional[int]
    CARRIER_DELAY: Union[float, None]
    WEATHER_DELAY: Union[float, None]
    NAS_DELAY: Union[float, None]
    SECURITY_DELAY: Union[float, None]
    LATE_AIRCRAFT_DELAY: Union[float, None]
    FIRST_DEP_TIME: Optional[str]
    TOTAL_ADD_GTIME: Optional[str]
    LONGEST_ADD_GTIME: Optional[str]
    Column65: Optional[str]


# 3. Class for training the model and making predictions
class LGBModel:
    # 6. Class constructor, loads the dataset and loads the model
    #    if exists. If not, calls the _train_model method and
    #    saves the model
    def __init__(self):
        self.model_fname_ = 'model.pkl'
        self.model = joblib.load(self.model_fname_)

    # 5. Make a prediction based on the user-entered data
    #    Returns the predicted species with its respective probability
    def predict_delay(self, QUARTER , MONTH , DAY_OF_MONTH , DAY_OF_WEEK , ORIGIN_AIRPORT_ID , DEST_AIRPORT_ID , DEP_TIME , ARR_TIME , VACATION):
        data_in = [[ QUARTER , MONTH , DAY_OF_MONTH , DAY_OF_WEEK , ORIGIN_AIRPORT_ID , DEST_AIRPORT_ID , DEP_TIME , ARR_TIME , VACATION]]
        prediction = self.model.predict(data_in)
        # probability = self.model.predict_proba(data_in).max()
        # return prediction[0], probability
        return prediction[0]
