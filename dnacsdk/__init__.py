"""The __init__.py file is called whenever someone imports the package into their program."""

import logging
from .dnac import DNAC
from .api_objects import (
    ApplicationPolicy,
    Authentication,
    Clients,
    CommandRunner,
    ConfigurationTemplates,
    DeviceOnboarding,
    Devices,
    EventManagement,
    File,
    Issues,
    NetworkDiscovery,
    NetworkSettings,
    NonFabricWireless,
    PathTrace,
    SDA,
    SiteDesign,
    Sites,
    SWIM,
    Tag,
    Task,
    Topology,
    Users,
)

logging.debug("In the dnacsdk __init__.py file.")


def __authorship__():
    """
    Authorship and gratitude for contributors.

    This python module was created by Dax Mickelson  Feel free to send comments/suggestions/improvements.  Either by
    email: dmickels@cisco.com or more importantly via a pull request from the github repository:
    https://github.com/daxm/dnacsdk.
    """
    logging.debug(__authorship__.__doc__)


__authorship__()
