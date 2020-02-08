# DNA Center SDK
Network automation and programming through the use of APIs is upon us.  However, the typical network engineer doesn't
have the programming skills to directly interact with the APIs being produced by companies.  So, a "helper" program is
needed.  This dnacsdk Python package is just such a tool.

## Structure and Layout
The layout of the modules in this package have been organized to match the DNA Center API documenation.  (The latest
doc being: ![https://developer.cisco.com/docs/dna-center/api/1-3-3-x/](https://developer.cisco.com/docs/dna-center/api/1-3-3-x/).)

## How to use
First, import this package into your Python script.
```python
import dnacsdk
```

To start you need to create an object that has the connection details for communicating with DNA Center.
```python
my_dnac = dnacsdk.DNAC(blah)
```

With the connection parameters set up you can now interact with the various helper functions related to the DNA Center
API actions.  Most of the helper functions are named the same as their related DNA Center API is named.

For example, the Site API lists 8 actions (2 POST, 4 GET, 1 DELETE, and 1 PUT actions).
The first API action is a POST action to /dna/system/api/v1/site/{siteID}/device and is for "Assigning a device to Site".
In dnacsdk this would be accessed as follows:
```python
import dnacsdk

my_dnac = dnacsdk.DNAC(blah)

result = dnacsdk.sites.assign_devices_to_site(site_name="name of site", devices=[ list of device names])
```

The dnacsdk.sites.assign_devices_to_site() helper function will use the the site_name and devices variables to gather
the pertinent information and send the API call to DNA Center.  It will then return the response from the API call (and
in this case assign that response to the result variable).

What you don't see or need to know about is that the /dna/system/api/v1/site/{siteID}/device API action has particular
formatting and minimum information needed in order to successfully perform the action.  In this case it needs the site's
ID and the devices IPs (formatted in a list of dictionaries with the "ip" attribute assigned in each dictionary).  The
dnacsdk.sites.assign_devices_to_site() helper function will gather and format that information for you.
