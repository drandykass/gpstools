import gpxpy
import datetime
import utm
import numpy as np
import copy

class gps:
    """
    Class for handling of gps data in a field-survey setting.

    """

    #Holds list of dicts for original data points
    wypts = []
    
    def load_gpx(self,fname):
        """
        Load gps data into class members from a gpx file.

        .. Note: For optimum performance and utility, only put one line 
            of data into a single gps object. Most utilities assume all
            GPS data are from a single transect.

        Reads a gpx file using gpxpy and parses into a list of dictionaries.

        Parameters:

        * fname : string
            File name to be read in

        Returns:

        * self.wypts : Pointer
            Pointer to a list of dictionary objects containing the data

        """

        try:
            fgpx = open(fname,'r')
        except IOError:
            print 'Error reading', fname
            return 1
        gpx = gpxpy.parse(fgpx)
        for w in gpx.waypoints:
            t = {'name':str, 'lat':float, 'long':float, 'elev':float,
                'time':datetime, 'easting':float, 'northing':float,
                'utmzone':int, 'utmlet':str}
            t['name'] = w.name
            t['lat'] = w.latitude
            t['long'] = w.longitude
            t['elev'] = w.elevation
            t['time'] = w.time
            t['easting'], t['northing'], t['utmzone'], t['utmlet'] = self.latlongtoUTM(t['lat'], t['long'])
            self.wypts.append(copy.deepcopy(t))
        fgpx.close()
        return self.wypts


