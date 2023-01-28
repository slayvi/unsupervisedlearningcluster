import pandas as pd
import datetime
import numpy as np


def feature_selecting_part_1(filename_full_data, filename_to_save):
     """ 
     Load Dataset from JSON-File and save it to filename_to_save with abstract and categories only 
     """

     print(" Loading Data... ".center(120, "="))
     data_full = pd.read_json(filename_full_data, lines=True, encoding="utf-8")

     df = data_full[["title", "abstract", "versions"]]
     print(f" Data with Filename {filename_full_data} was loaded successfully. ".center(120, "="))
     print(" Abstract, Title and Versions were collected. Looking for latest version... ".center(120, "="))


     # Parse to Series to make the versions accessible:
     temp_frame = df["versions"].apply(pd.Series)

     # None Values existing through the command above will be replaced by last seen value (latest version):
     temp_frame = temp_frame.fillna(axis = "columns", method="ffill")
     last_column = len(temp_frame.columns)

     df["latest_version"] = temp_frame[last_column-1]

     # Set the latest time to consider samples:
     latest_date_to_consider = datetime.datetime(2022, 3, 1, 0, 0, 0)

     print(f" Dates were extractet, checking now for samples newer than {latest_date_to_consider}. ".center(120, "="))

     # Checks if sample is newer than latest_date_to_consider and set it to NaN otherwise:
     date_parsed = []
     for _ in range(len(df.index)):

          date_temp = datetime.datetime.strptime(df["latest_version"][_]["created"], "%a, %d %b %Y %H:%M:%S %Z")
               
          if date_temp > latest_date_to_consider:
               date_parsed.append(date_temp)
          else:
               date_parsed.append(np.nan)

     # List the parsed dates to the Dataframe and drop all Rows with NaN (older than latest_date_to_consider):
     df["version_keep"] = date_parsed
     df = df.dropna(subset = ['version_keep'])

     # Drop columns which are not needed anymore:
     df = df.drop(columns="versions")
     df = df.drop(columns="latest_version")

     print(f" Sucessfully dropped samples which are older than {latest_date_to_consider}. ".center(120, "="))

     print(" Checking for samples with no Data: ".center(120, "="))
     print(df.isnull().sum())

     df = df.drop(columns="version_keep")

     # reset the index and drop columns with the old ones
     df = df.reset_index()
     df = df.drop(columns="index")

     print(" Head of File will look like the following: ".center(120, "="))
     print(df.head(3))
     print(f" Data will be stored in {filename_to_save}... ".center(120, "="))

     df = df.to_json(filename_to_save)
     print(f" Successfully stored dataset in {filename_to_save}. ".center(120, "="))



if __name__ == "__main__":

     print("")
     print("=".center(120, "="))
     print(" Hello and Welcome! ".center(120, "="))
     print("=".center(120, "="))

     feature_selecting_part_1(filename_full_data = "data/arxiv-metadata-oai-snapshot.json", 
                              filename_to_save = "data/data_selected.json")