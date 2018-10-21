# -*- coding: utf-8 -*-
"""
    pixela.client
    ~~~~~~~~~~~~~

    Pixela client.


    :copyright: (c) 2018 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
from datetime import datetime


class GraphMethodsMixin(object):

    def create_graph(self, graph_id, name, unit, type, color):
        params = {
            'id': graph_id,
            'name': name,
            'unit': unit,
            'type': type,
            'color': color,
        }
        return self.send(
            method='post',
            url='users/{username}/graphs'.format(username=self.username),
            params=params,
            token=self.token,
        )

    def get_graphs(self):
        return self.send(
            method='get',
            url='users/{username}/graphs'.format(username=self.username),
            params=None,
            token=self.token,
        )

    def graph_url(self, graph_id, date=None):
        url = '{endpoint}/users/{username}/graphs/{graph_id}'.format(
            endpoint=self.API_ENDPOINT,
            username=self.username,
            graph_id=graph_id,
        )
        if date:
            url = url + '?date={date}'.format(date=self.to_ymd(date))

        return url

    def update_graph(self, graph_id, name, unit, color, purge_cache_urls=None):
        params = {
            'name': name,
            'unit': unit,
            'color': color,
        }
        if purge_cache_urls:
            params['purge_cache_urls'] = purge_cache_urls \
                if isinstance(purge_cache_urls, list) else [purge_cache_urls]

        return self.send(
            method='put',
            url='users/{username}/graphs/{graph_id}'.format(
                username=self.username,
                graph_id=graph_id,
            ),
            params=params,
            token=self.token,
        )

    def delete_graph(self, graph_id):
        return self.send(
            method='delete',
            url='users/{username}/graphs/{graph_id}'.format(
                username=self.username,
                graph_id=graph_id,
            ),
            params=None,
            token=self.token,
        )


class PixelMethodsMixin(object):

    def create_pixel(self, graph_id, quantity, date=None):
        if not date:
            date = datetime.now(self.tz).today()

        params = {
            'date': self.to_ymd(date),
            'quantity': str(quantity),
        }
        return self.send(
            method='post',
            url='users/{username}/graphs/{graph_id}'.format(
                username=self.username,
                graph_id=graph_id,
            ),
            params=params,
            token=self.token,
        )

    def get_pixel(self, graph_id, date=None):
        if not date:
            date = datetime.now(self.tz).today()

        return self.send(
            method='get',
            url='users/{username}/graphs/{graph_id}/{date}'.format(
                username=self.username,
                graph_id=graph_id,
                date=self.to_ymd(date),
            ),
            params=None,
            token=self.token,
        )

    def update_pixel(self, graph_id, quantity, date=None):
        if not date:
            date = datetime.now(self.tz).today()

        params = {
            'quantity': str(quantity),
        }

        return self.send(
            method='put',
            url='users/{username}/graphs/{graph_id}/{date}'.format(
                username=self.username,
                graph_id=graph_id,
                date=self.to_ymd(date),
            ),
            params=params,
            token=self.token,
        )

    def delete_pixel(self, graph_id, date):
        return self.send(
            method='delete',
            url='users/{username}/graphs/{graph_id}/{date}'.format(
                username=self.username,
                graph_id=graph_id,
                date=self.to_ymd(date),
            ),
            params=None,
            token=self.token,
        )

    def increment_pixel(self, graph_id):
        return self.send(
            method='put',
            url='users/{username}/graphs/{graph_id}/increment'.format(
                username=self.username,
                graph_id=graph_id,
            ),
            params=None,
            token=self.token,
        )

    def decrement_pixel(self, graph_id):
        return self.send(
            method='put',
            url='users/{username}/graphs/{graph_id}/decrement'.format(
                username=self.username,
                graph_id=graph_id,
            ),
            params=None,
            token=self.token,
        )


class UserMethodsMixin(object):

    def create_user(self, agree_terms_of_service, not_minor):
        params = {
            'token': self.token,
            'username': self.username,
            'agreeTermsOfService': 'yes' if agree_terms_of_service is True else 'no',
            'notMinor': 'yes' if agree_terms_of_service is True else 'no',
        }

        return self.send(method='post', url='users', params=params)

    def update_user(self, new_token):
        params = {
            'newToken': new_token,
        }
        return self.send(
            method='put',
            url='users/{username}'.format(username=self.username),
            params=params,
            token=self.token,
        )

    def delete_user(self):
        return self.send(
            method='delete',
            url='users/{username}'.format(username=self.username),
            token=self.token,
        )


class WebhookMethodsMixin(object):

    def create_webhook(self, graph_id, type):
        params = {
            'graphID': graph_id,
            'type': type,
        }
        return self.send(
            method='post',
            url='users/{username}/webhooks'.format(
                username=self.username,
            ),
            params=params,
            token=self.token,
        )

    def get_webhook(self):
        return self.send(
            method='get',
            url='users/{username}/webhooks'.format(
                username=self.username,
            ),
            params=None,
            token=self.token,
        )

    def invoke_webhook(self, webhook_hash):
        return self.send(
            method='post',
            url='users/{username}/webhooks/{webhook_hash}'.format(
                username=self.username,
                webhook_hash=webhook_hash,
            ),
            params=None,
        )

    def delete_webhook(self, webhook_hash):
        return self.send(
            method='delete',
            url='users/{username}/webhooks/{webhook_hash}'.format(
                username=self.username,
                webhook_hash=webhook_hash,
            ),
            params=None,
            token=self.token,
        )
