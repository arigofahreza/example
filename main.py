import sys

import numpy as np
import pandas as pd
from pydantic import BaseModel, Field


class VehicleModel(BaseModel):
    id: str = Field(alias='VIN (1-10)')
    region: str = Field(alias='County')
    city: str = Field(alias='City')
    postal_code: str | None = Field(alias='Postal Code')
    model: str = Field(alias='Model')
    model_year: str = Field(alias='Model Year')


def read_file():
    df = pd.read_csv(
        'C:\\Users\\LaptopBaru_2206\\PycharmProjects\\example\\resource\\Electric_Vehicle_Population_Data.csv',
        delimiter=';',
        on_bad_lines='skip')
    df = df.replace({np.nan: None})
    print(df.head(20))
    for index, row in df.iterrows():
        print(VehicleModel(**row.to_dict()))
        sys.exit(0)


if __name__ == '__main__':
    read_file()
