""" 
Script to download all PRISM and REGION WWWDT Climate Datasets (NetCDF)
"""
import os

variables = ['mdn','pon', 'spi','spei', 'pdsi','scpdsi','pzi']
months = [1,2,3,4,5,6,7,8,9,10,11,12]
month_span = [1,2,3,4,5,6,7,8,9,10,11,12]
month_span_extended = [15,18,24,30,36,48,60,72]
data_url = "http://wrcc.dri.edu/monitor/WWDT/data/"
data_types = ["PRISM", "REGIONS"]

def download_file(url):
    """Downnload a file using wget or update file if newer version exists """
    os.system("wget -cN %s" % url)

def get_data(data_type):
    """Download the Climate Data based on data type PRISM or REGIONS"""

    for variable in variables:
        for month in months:
            # 1 = Jan 3=Mar ect
            month = str(month)
    
            # Variables with no month span
            if variable == 'pdsi' or variable == 'scpdsi' or variable == 'pzi':
                url = data_url + data_type + "/" + variable + "/" + variable + "_" + month + "_"+ data_type+ ".nc" 
                download_file(url)

            # Variables with month span
            else:
                # Get month spans 1-12 
                for span in month_span:
                    span = str(span)
                    url = data_url + data_type + "/" + variable + span+ "/" + variable + span + "_" + month + "_"+ data_type+ ".nc" 
                    download_file(url)

                # Get extended month spans
                for span in month_span_extended:
                    span = str(span)
                    url = data_url + data_type + "/" + variable + span+ "/" + variable + span + "_" + month + "_"+ data_type+ ".nc" 
                    download_file(url)

# Uncomment following line to download PRISM data
#get_data(data_types[0])
# Uncomment following line to download REGIONS data
#get_data(data_types[1])
