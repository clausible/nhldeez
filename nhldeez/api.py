import requests as r
import json
from urllib.parse import urljoin

BASEURL = "https://statsapi.web.nhl.com/api/v1/"


def conferences(id: int = None) -> r.Response:
    url = urljoin(BASEURL, "conferences")
    if id:
        url = urljoin(url, str(id))
    return r.get(url)


def divisions(id: int = None) -> r.Response:
    url = urljoin(BASEURL, "divisions")
    if id:
        url = urljoin(url, str(id))
    return r.get(url)


def draft(year: int = None) -> r.Response:
    url = urljoin(BASEURL, "draft")
    if year:
        url = urljoin(url, str(year))
    return r.get(url)


def draft_prospects(id: int = None) -> r.Response:
    url = urljoin(BASEURL, "draft/prospects")
    if id:
        url = urljoin(url, str(id))
    return r.get(url)
