# -*- coding: utf-8 -*-
"""
    pixela
    ~~~~~~

    Pixela Python client.


    :copyright: (c) 2018 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
__version__ = '1.0.0'

import json
import logging
from datetime import datetime

from pytz import timezone
from requests import (
    HTTPError,
    Session,
)

from .client import (
    GraphMethodsMixin,
    PixelMethodsMixin,
    UserMethodsMixin,
    WebhookMethodsMixin,
)


class Pixela(
    GraphMethodsMixin,
    PixelMethodsMixin,
    UserMethodsMixin,
    WebhookMethodsMixin,
):
    API_ENDPOINT = 'https://pixe.la/v1'

    headers = {
        'User-Agent': 'Pixela v{version} (https://github.com/heavenshell/py-pixela)'.format(version=__version__),
        'Content-Type': 'application/json',
    }

    def __init__(self, username, token, tz=None, logger=None):
        self.username = username
        self.token = token
        tz = tz or 'UTC'
        self.tz = timezone(tz)

        if logger is None:
            log_format = (
                '[%(asctime)s %(levelname)s][%(pathname)s:%(lineno)d]: %(message)s'
            )
            logging.basicConfig(level=logging.INFO, format=log_format)
            logger = logging.getLogger('pixela')

        self.logger = logger

    def send(self, method, url, params=None, token=None):
        try:
            session = Session()
            session.headers = self.headers
            if token is not None:
                session.headers.update({'X-USER-TOKEN': token})

            endpoint = '{base_url}/{url}'.format(
                base_url=self.API_ENDPOINT,
                url=url,
            )
            data = json.dumps(params) if params else None
            if method == 'get':
                res = session.get(endpoint, params=data)
            elif method == 'post':
                res = session.post(endpoint, data=data)
            elif method == 'put':
                res = session.put(endpoint, data=data)
            elif method == 'delete':
                res = session.delete(endpoint)

            session.close()
            return res
        except HTTPError as e:
            self.logger.error(e)

    def to_ymd(self, date):
        assert(isinstance(date, datetime))
        return date.strftime('%Y%m%d')
