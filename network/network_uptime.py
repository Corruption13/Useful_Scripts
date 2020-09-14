"""
##################################################################################################### 
#                                                                                                   #
# S Sandeep Pillai                                                                                  #
# Simple Script that can be called to ping a custom ip address of choice and find the uptime of     #
# the network. Suggested to call function in a separate thread to your main application.            #
# Contact: https://github.com/Corruption13                                                          #
#                                                                                                   #
##################################################################################################### 
"""
from requests import get
import time
from datetime import datetime



def network_uptime(ip='1.1.1.1', sleep=3, header = "http://", debug=False):
    """
    #####################################################################################################
    #                                                                                                   #
    #       Function name: network_uptime()                                                             #
    #       Function arguments: ip_address(string), sleep(int), [header(string)]                        #
    #       Default arguments: "1.1.1.1", 3, "http://"                                                  #
    #       Optional 'debug' argument: Set to True for Console Output                                   #
    #                                                                                                   #
    #       Return: Dictionary of 3 values:                                                             #
    #           dict['init'] -> starting time (type= <class 'datetime.datetime'> )                      #
    #           dict['end'] -> terminate time (type= <class 'datetime.datetime'> )                      #
    #           dict['delta'] -> time delta  (type= <class 'datetime.timedelta'> )                      #
    #                                                                                                   #
    #####################################################################################################
    """
    connect = True
    start_time = datetime.now()
    if debug==True: print("Current time: ", start_time)
    while(connect == True):
    
        
        try:
            resp = get(header + ip) 

            if resp.status_code == 200:
                if debug==True: print(resp, " @ ", datetime.now().strftime("%H:%M:%S"))
            else:
                if debug==True: print ('\nDisconnected!\n')
                connect = False 

            time.sleep(sleep)

        except:
            if debug==True: print ('\nDisconnected!\n')
            connect = False 
    
    end_time = datetime.now()
    
    values = {
        'init':  start_time,
        'end':  end_time,
        'delta': ( end_time - start_time) 
    }


    if debug==True: 
        print("Started Ping at: ", values['init'])          # Start time
        print("Disconnected at: ", values['end'])           # End time
        print("Network up for: ", values['delta'])          # Time delta

    return values 


#####################################################################################################
#                                                                                                   #
# Main function below                                                                               #
#                                                                                                   #
#####################################################################################################

if __name__ == "__main__":
    import sys 
    


    if len(sys.argv) ==3:
        ip = sys.argv[1]
        sleep = float(sys.argv[2])
        print("\nUsing sys arg values for ip and sleep: \n")
        print(ip, " ", sleep)
        network_uptime(ip, sleep, debug=True)
    
    else:
        print("\nNo command line arguments given, using default values ( ip = 1.1.1.1, sleep = 5 sec )")
        print("\nTo use command args, call script as -> [ network_uptime.py ip_addresss sleep_timer_number ]\n")
        network_uptime(debug=True)

    print("~ showing docs in 7 seconds")
    time.sleep(7)

    help(network_uptime)
    print("\n\nWant to use this functon in your application? Just follow the docs above! \n")

