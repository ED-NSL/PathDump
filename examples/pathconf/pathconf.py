import ctrlapi as capi
import sys

#Pathconformance application checks paths in each flow record. For simplicity, this app define path with length > 4 as abnormal and
#raises alarm to controller.
if __name__ == "__main__":
    tree = capi.getAggTree (['controller'])
    subscr_url = "tcp://localhost:5556"
    filter_str = "TIB "
    interval = 0.001
    query = {'name': 'pathconf_check.py', 'argv': [subscr_url,filter_str]}
    
    if len (sys.argv) == 2 and sys.argv[1] == 'uninstall':
        data = capi.uninstallQuery (tree, query)
    else:
        data = capi.installQuery (tree, query, interval) 

    
