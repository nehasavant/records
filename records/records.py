#!/usr/bin/env python

import pandas as pd
import requests

class Records:
    def __init__(self, q=None, interval=None):
        
        self.q = q
        self.interval = str(interval[0]) + "," + str(interval[1])
        self.params = {
            "q":self.q,
            "year":self.interval, #can enter as such bc GBIF API can handle a two integer interval (a tuple?)
            "basisOfRecord": "PRESERVED_SPECIMEN",    
            "hasCoordinate": "true",
            "hasGeospatialIssue": "false",
            "country": "US",
            "offset":"0",
            "limit":"300"
        }
        self.df = pd.DataFrame() #Need to initialize empty dataframe to fill it later, and call it outside the class
        
        self._get_all_records()

    #private function
    def _get_all_records(self):
        "iterate until end of records"
        data = []
    
        while 1: # Using 1 here is another way of saying True. If you use 1 or True, you MUST have a break statement to stop the loop.
        # make request and store results. Remember the results will be a JSON dictionary.
            self.res = requests.get(
            url="http://api.gbif.org/v1/occurrence/search?", 
            params=self.params
            )
            # increment counter
            self.params["offset"] = str(int(self.params["offset"]) + 300)
          
            self.res.raise_for_status()
            # concatenate data 
            
            idata = self.res.json()
            data += idata["results"]

            # #increment years when endOfRecords for that year is reached
            if idata["endOfRecords"]:
                break
                
        self.df = pd.DataFrame(data)
        
        return self.df