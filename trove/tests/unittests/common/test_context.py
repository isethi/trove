# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
import trove.common.context as context

import testtools
from testtools.matchers import Equals, Is


class TestTroveContext(testtools.TestCase):
    def test_create_with_extended_args(self):
        ctx = context.TroveContext(user="test_user_id",
                                   request_id="test_req_id",
                                   limit="500",
                                   marker="x")
        self.assertThat(ctx.limit, Equals("500"))
        self.assertThat(ctx.marker, Equals("x"))

    def test_create(self):
        ctx = context.TroveContext(user='test_user_id',
                                   request_id='test_req_id')
        self.assertThat(ctx.user, Equals('test_user_id'))
        self.assertThat(ctx.request_id, Equals('test_req_id'))
        self.assertThat(ctx.limit, Is(None))
        self.assertThat(ctx.marker, Is(None))

    def test_to_dict(self):
        ctx = context.TroveContext(user='test_user_id',
                                   request_id='test_req_id')
        ctx_dict = ctx.to_dict()
        self.assertThat(ctx_dict.get('user'), Equals('test_user_id'))
        self.assertThat(ctx_dict.get('request_id'), Equals('test_req_id'))
