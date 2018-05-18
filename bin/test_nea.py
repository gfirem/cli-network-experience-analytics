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

import nea
import unittest

CSV_NEWLINE = '\r\n'


class ReportToCsvTestCase(unittest.TestCase):
    def setUp(self):
        self.multi_kpi_report = {
            'kpis': [
                'Plays with Rebuffers',
                'Startup Time',
                'Bitrate'
            ],
            'series': [
                {
                    'dimensions': [],
                    'data': [
                        [
                            '2018-01-01T05:00:00.000Z',
                            19.18,
                            2.13,
                            1558.96
                        ],
                        [
                            '2018-01-02T05:00:00.000Z',
                            18.92,
                            2.19,
                            1527.2
                        ]
                    ],
                    'maxDate': '2018-01-07T05:00:00.000Z',
                    'minDate': '2018-01-10T05:00:00.000Z',
                    'avg': 1517.4093333333333,
                    'min': 1414.6,
                    'max': 1588.39,
                    'percentile2': 1418.6263999999999,
                    'percentile50': 1533.64,
                    'percentile98': 1581.3816
                }
            ]
        }

    def test_multi_kpi(self):
        self.assertEqual(
            nea.report_to_csv(self.multi_kpi_report, ['time']),
            CSV_NEWLINE.join([
                'time,Plays with Rebuffers,Startup Time,Bitrate',
                '2018-01-01T05:00:00.000Z,19.18,2.13,1558.96',
                '2018-01-02T05:00:00.000Z,18.92,2.19,1527.2'
            ]) + CSV_NEWLINE
        )


if __name__ == '__main__':
    unittest.main()
