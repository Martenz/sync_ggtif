# -*- coding: utf-8 -*-
#!/usr/bin/python

### Service to Sync deleted geotiff from Geonode with Geoserver folder
### the service delete all geoserver folders which does not have
### the correspondig geotiff file in the geonode folder

### To run the service:     "python sync_ggtif_service.py start"
### To stop the service:    "python sync_ggtif_service.py stop"
### To restart the service: "python sync_ggtif_service.py restart"

import sys
import os
import shutil
import time
from daemon import runner

########### main path ###############################################################

geonode_uploaded_dir = 'yourpath..\\geonode\\'
geoserver_data_dir = 'yourpath..\\geoserver\\'
extension = '.tif'

#####################################################################################

class App():
        def __init__(self):
                self.stdin_path = '/dev/null'
                self.stdout_path = '/dev/tty'
                self.stderr_path = '/dev/tty'
                self.pidfile_path =  '/tmp/foo.pid'
                self.pidfile_timeout = 5
        def run(self):
            while True:
                f_list_geonode_uploaded_dir = [ geonode_uploaded_dir+f for f in os.listdir(geonode_uploaded_dir) if len(os.path.splitext(f))>1 ]
                f_list_geotiff_geonode_uploaded_dir = [ f for f in f_list_geonode_uploaded_dir if os.path.splitext(f)[1]==extension ]

                d_list_geoserver_data_dir = [ d for d in os.listdir(geoserver_data_dir) if os.path.splitext(d)[1]=='' ]

                for d in d_list_geoserver_data_dir:
                        #print 'Folder: '+str(d)
                        if not os.path.exists(geonode_uploaded_dir + d + extension):
                                shutil.rmtree(geoserver_data_dir+d)
                                #print geonode_uploaded_dir + d + extension, 'not found'
                                #print 'folder: ',d,'deleted'
                time.sleep(1)

app = App()
deamon_runner = runner.DeamonRunner(app)
deamon_runner.do_action()
