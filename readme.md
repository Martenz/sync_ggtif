Sync deleted geotiff Geonode and Geoserver folders
===============
 Service to Sync deleted geotiff from Geonode with Geoserver folder the service delete all geoserver folders which does not have the correspondig geotiff file in the geonode folder.

GeoNode Installation
====================

To run the service::

    python sync_ggtif_service.py start

To stop the service::

    python sync_ggtif_service.py stop

To restart the service::

    python sync_ggtif_service.py restart
