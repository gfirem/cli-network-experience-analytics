# Copyright 2018 Akamai Technologies, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import csv
import io

logger = logging.getLogger('nea')
logger.setLevel(logging.DEBUG)


class NeaClient(object):
    """Encapsulates the NEA API.

    Any interaction with the NEA API requires an instance of
    this class.

    To consume the API using different authorizations (for example, read-only
    vs. read/write), allocate separate instances of this class, providing
    different connected sessions to __init__().
    """

    def __init__(self, session, host):
        """Initializes an NeaClient instance.

        Args:
            session (object): A connected Python Requests session.

            host (string): Host name of the API server, provided by the Luna
                "Manage APIs" app Authorization Details dialog.
                For example "akab-xxxxxxxxxxxxxxxx-yyyyyyyyyyyyyyyy.luna.akamaiapis.net".
                Note that this does not include the scheme ("https://").
        """
        self._session = session
        self._base_url = self._make_api_url(host)

    # Public members
    # --------------
    def get_service_version(self):
        return self._session.get(self._base_url + '/app/version')

    def get_report(self,
                   start_time,
                   end_time,
                   network_operator_id,
                   group_id,
                   report_granularity,
                   kpis=None,
                   ungrouped_dims=None,
                   grouped_dims=None):
        url_params = {
            'startTime': start_time,
            'endTime': end_time,
            'gid': group_id,
            'reportGranularity': report_granularity
        }

        if ungrouped_dims:
            i = 0
            for dim in ungrouped_dims:
                url_params['ud' + str(i + 1)] = dim
                i += 1

        if grouped_dims:
            i = 0
            for dim in grouped_dims:
                url_params['gd' + str(i + 1)] = dim
                i += 1

        if kpis:
            i = 0
            for kpi in kpis:
                url_params['kpi' + str(i + 1)] = kpi
                i += 1

        return self._get(
            self._base_url +
            '/customers/%u/reports' % network_operator_id,
            params=url_params
        )

    # Private members
    # ---------------
    @staticmethod
    def _make_api_url(host):
        return ''.join([
            'https://',
            host,
            '/',
            'nea/v1'
        ])

    def _get(self, url, params=None):
        result = self._session.get(url, params=params)
        result.raise_for_status()
        return result


def report_to_csv(report, ungrouped_dimensions):
    csv_output = io.StringIO()
    writer = csv.writer(csv_output)

    writer.writerow(ungrouped_dimensions + report['kpis'])

    for row in report['series'][0]['data']:
        writer.writerow(row)

    result = csv_output.getvalue()
    csv_output.close()
    return result
