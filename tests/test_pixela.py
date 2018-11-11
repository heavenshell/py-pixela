# -*- coding: utf-8 -*-
"""
    pixela.tests
    ~~~~~~~~~~~~

    Tests for pixela.


    :copyright: (c) 2018 Shinya Ohyanagi, All rights reserved.
    :license: BSD, see LICENSE for more details.
"""
import json
from datetime import datetime
from unittest import TestCase

from mock import mock
from requests import (
    Response,
    Session,
)

from pixela import Pixela


def mock_response(status_code, content):
    res = Response()
    res.status_code = status_code
    res._content = json.dumps(content)

    return res


class UserMethodsMixinTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Pixela(username='heavenshell', token='ba0afe74-86a3-40fe-8bf7-0801027d087d')

    def test_deprecation_warning(self):
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.filterwarnings('always')
            Pixela(
                username='heavenshell',
                token='ba0afe74-86a3-40fe-8bf7-0801027d087d',
                tz='Asia/Tokyo',
            )
            self.assertEqual(str(w.pop().message), 'tz will remove 1.3.0')

    @mock.patch.object(
        Session,
        'post',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_create_user(self, m):
        res = self.client.create_user(
            agree_terms_of_service=True,
            not_minor=True,
        )
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'put',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_update_user(self, m):
        res = self.client.update_user(new_token='ba0afe74-86a3-40fe-8bf7-0801027d087d')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'delete',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_delete_user(self, m):
        res = self.client.delete_user()
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)


class GraphMethodsMixinTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Pixela(
            username='heavenshell',
            token='ba0afe74-86a3-40fe-8bf7-0801027d087d',
        )

    @mock.patch.object(
        Session,
        'post',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_create_graph(self, m):
        res = self.client.create_graph(
            graph_id='py-pixela',
            name='py-pixela',
            unit='commit',
            type='int',
            color='shibafu',
            timezone='Asia/Tokyo',
        )
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'get',
        return_value=mock_response(
            status_code=200,
            content={'graphs': [{
                'id': 'py-pixela', 'name': 'py-pixela',
                'unit': 'commit', 'type': 'int', 'color': 'momiji',
                'purgeCacheURLs': None,
            }]},
        ),
    )
    def test_get_graphs(self, m):
        res = self.client.get_graphs()
        ret = json.loads(res.content)
        self.assertEqual(ret['graphs'][0]['id'], 'py-pixela')

    @mock.patch.object(
        Session,
        'put',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_update_graph(self, m):
        res = self.client.update_graph(
            graph_id='py-pixela',
            name='py-pixela',
            unit='commit',
            color='momiji',
            timezone='GMT',
        )
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    def test_get_url(self):
        url = self.client.graph_url(graph_id='py-pixela')
        self.assertEqual(url, 'https://pixe.la/v1/users/heavenshell/graphs/py-pixela')

        date = datetime.strptime('2018-10-21', '%Y-%m-%d')
        url = self.client.graph_url(graph_id='py-pixela', date=date)
        self.assertEqual(url, 'https://pixe.la/v1/users/heavenshell/graphs/py-pixela?date=20181021')

        url = self.client.graph_url(graph_id='py-pixela', mode='short')
        self.assertEqual(url, 'https://pixe.la/v1/users/heavenshell/graphs/py-pixela?mode=short')

        url = self.client.graph_url(graph_id='py-pixela', date=date, mode='short')
        self.assertEqual(url, 'https://pixe.la/v1/users/heavenshell/graphs/py-pixela?date=20181021&mode=short')

    @mock.patch.object(
        Session,
        'delete',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_delete_graph(self, m):
        res = self.client.delete_graph(graph_id='py-pixela')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)


class PixelMethodsMixinTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Pixela(username='heavenshell', token='ba0afe74-86a3-40fe-8bf7-0801027d087d')

    @mock.patch.object(
        Session,
        'post',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_create_pixel(self, m):
        res = self.client.create_pixel(graph_id='py-pixela', quantity=5)
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'get',
        return_value=mock_response(
            status_code=200,
            content={'quantity': 5},
        ),
    )
    def test_get_pixel(self, m):
        date = datetime.strptime('2018-10-21', '%Y-%m-%d')
        res = self.client.get_pixel(graph_id='py-pixela', date=date)
        ret = json.loads(res.content)
        self.assertEqual(ret['quantity'], 5)

    @mock.patch.object(
        Session,
        'put',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_update_pixel(self, m):
        date = datetime.strptime('2018-10-21', '%Y-%m-%d')
        res = self.client.update_pixel(
            graph_id='py-pixela',
            quantity=30,
            date=date,
        )
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'delete',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_delete_pixel(self, m):
        date = datetime.strptime('2018-10-21', '%Y-%m-%d')
        res = self.client.delete_pixel(
            graph_id='py-pixela',
            date=date,
        )
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'put',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_increment_pixel(self, m):
        res = self.client.increment_pixel(graph_id='py-pixela')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'put',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_decriment_pixel(self, m):
        res = self.client.decrement_pixel(graph_id='py-pixela')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)


class WebhookMethodsTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = Pixela(username='heavenshell', token='ba0afe74-86a3-40fe-8bf7-0801027d087d')

    @mock.patch.object(
        Session,
        'post',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True, 'webhookHash': 'xxx'},
        ),
    )
    def test_webhook_create(self, m):
        res = self.client.create_webhook(graph_id='py-pixela', type='increment')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)
        self.assertEqual(ret['webhookHash'], 'xxx')

    @mock.patch.object(
        Session,
        'get',
        return_value=mock_response(
            status_code=200,
            content={
                'hashString': 'xxx',
                'graphID': 'py-pixela',
                'type': 'increment',
            },
        ),
    )
    def test_get_webhook(self, m):
        res = self.client.get_webhook()
        ret = json.loads(res.content)
        self.assertEqual(ret['hashString'], 'xxx')
        self.assertEqual(ret['graphID'], 'py-pixela')
        self.assertEqual(ret['type'], 'increment')

    @mock.patch.object(
        Session,
        'post',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_invoke_webhook(self, m):
        res = self.client.invoke_webhook(webhook_hash='xxx')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)

    @mock.patch.object(
        Session,
        'delete',
        return_value=mock_response(
            status_code=200,
            content={'message': 'Success.', 'isSuccess': True},
        ),
    )
    def test_webhook_delete(self, m):
        res = self.client.delete_webhook(webhook_hash='xxx')
        ret = json.loads(res.content)
        self.assertEqual(ret['message'], 'Success.')
        self.assertEqual(ret['isSuccess'], True)
