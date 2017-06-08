import numpy as np


class GPS_Time:
        def __init__(self, year, month, day, hour_fraction):                   
            self.sow = self.julian_day_conversion(year, month, day, hour_fraction)

        #Conversion only valid 01.03.1990-28.02.2100
        def julian_day_conversion(self, year, month, day, hour_fraction):
            if month <= 2:
                year = year -1
                month = month +12
            julian_day = np.floor(365.25*(year+4716)) + np.floor(30.6001*(month+1)) +day + hour_fraction/24-1537.5
            sow = self.gps_time(julian_day)

            return sow
        

        #Conversion of Julian Day number to GPS week and "Seconds of week" (sow) as from Saturday midnight
        def gps_time(self, julian_day):
            a = np.floor(julian_day +0.5);
            b = a+1537
            c = np.floor((b-122.1)/365.25)
            e = np.floor(365.25 * c)
            f = np.floor((b-e)/30.6001)
            d = b-e-np.floor(30.6001*f)+np.remainder(julian_day+0.5, 1)
            day_of_week = np.remainder(np.floor(julian_day +0.5), 7)
            week = np.floor((julian_day - 2444244.5)/7)
            sow = (np.remainder(d, 1) + day_of_week +1) * 86400   #Add +1 as the GPS week starts at Saturday midnight
            
            return sow