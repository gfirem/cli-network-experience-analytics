[![Build Status](https://travis-ci.org/gfirem/cli-network-experience-analytics.svg?branch=master)](https://travis-ci.org/gfirem/cli-network-experience-analytics)

# Akamai CLI for Network Experience Analytics

The Network Experience Analytics (NEA) CLI provides you with statistics that depict the media, web, server, and network content quality of experience (QoE) your users have when accessing content from your network.

## Install

_NOTE_: This tool is intended to be installed via the [Akamai CLI](https://github.com/akamai/cli) package manager, which can be retrieved from the [releases](https://github.com/akamai/cli/releases) page of the Akamai CLI tool.

```
$ akamai install network-experience-analytics
```

## Usage
```bash
$ akamai network-experience-analytics <command>
```

You can also use the `nea` alias instead of `network-experience-analytics`, like so:
```bash
$ akamai nea <command>
```

The [Actions](#Actions) section describes the available commands.

## Actions
* [service-version](#service-version) - Retrieve the API service provider version.
* [report](#report) - Query the API for a network experience report.

## service-version
Retrieve the API service provider version.

### Flags
```
usage: akamai network-experience-analytics service-version [--edgerc EDGERC]
                                                           [--section SECTION]

optional arguments:
  --edgerc EDGERC    full path to the .edgerc file
  --section SECTION  a section of the .edgerc to use
```

### Example
```bash
$ akamai network-experience-analytics service-version
```

Output:
```
Getting service version... [OK]
{"version":"2.16.1-RELEASE","buildTimestamp":"2017-10-31T22:46:34436Z"}
```

## report
Query the API for a network experience report.

### Flags
```
usage: akamai network-experience-analytics report [-j | -c] -g GROUP_ID
                                                  [--edgerc EDGERC]
                                                  [--section SECTION] -o
                                                  NETWORK_OPERATOR_ID -s
                                                  START_TIME -e END_TIME
                                                  [-k KPI [KPI ...]]
                                                  [-d DIMENSION [DIMENSION ...]]
                                                  [-u DIMENSION [DIMENSION ...]]
                                                  [-G REPORT_GRANULARITY]

optional arguments:
  -j, --json            format output as JSON
  -c, --csv             format output as CSV
  -g GROUP_ID, --group-id GROUP_ID
                        Luna portal group (context) numeric identifier
  --edgerc EDGERC       full path to the .edgerc file
  --section SECTION     a section of the .edgerc to use
  -o NETWORK_OPERATOR_ID, --network-operator-id NETWORK_OPERATOR_ID
                        network operator numeric identifier
  -s START_TIME, --start-time START_TIME
                        start time of the report, in ISO-8601 format
  -e END_TIME, --end-time END_TIME
                        end time of the report, in ISO-8601 format
  -k KPI [KPI ...], --kpis KPI [KPI ...]
                        list of KPIs to include in the report
  -d DIMENSION [DIMENSION ...], --ungrouped-dimensions DIMENSION [DIMENSION ...]
                        list of ungrouped dimensions to include in the report
  -u DIMENSION [DIMENSION ...], --grouped-dimensions DIMENSION [DIMENSION ...]
                        list of dimensions by which to group KPIs and other
                        (ungrouped) dimensions
  -G REPORT_GRANULARITY, --report-granularity REPORT_GRANULARITY
                        granularity of report data, in seconds
```

Valid values for the `--kpis` argument:

| KPI Description                |  Argument Value             |
|--------------------------------|-----------------------------|
| Average Bitrate                |  avg-bitrate                |
| Average Rebuffer Time per Play |  avg-rebuffer-time-per-play |
| Average Throughput             |  avg-throughput             |
| Bandwidth                      |  bandwidth                  |
| Bitrate                        |  bitrate                    |
| Bytes                          |  bytes                      |
| Client First Byte Time         |  client-first-byte-time     |
| Client Throughput              |  client-throughput          |
| DNS Lookup Time                |  dns-lookup-time            |
| Downshifts per Play            |  downshifts-per-play        |
| First Paint Time               |  first-paint-time           |
| Hits                           |  hits                       |
| Media QoE                      |  media-qoe                  |
| Overall QoE                    |  overall-qoe                |
| Page Load Time                 |  page-load-time             |
| Play Duration                  |  play-duration              |
| Plays with Rebuffers           |  plays-with-rebuffers       |
| Plays                          |  ma-hits                    |
| Rebuffer Time per Minute       |  rebuffer-time-per-minute   |
| Rebuffers per Minute           |  rebuffers-per-minute       |
| Round Trip Time                |  round-trip-time            |
| Signal Strength                |  signal-strength            |
| Startup Abandonment Rate       |  startup-abandonment-rate   |
| Startup Time                   |  startup-time               |
| TCP Connection Time            |  tcp-connection-time        |
| Upshifts per Play              |  upshifts-per-play          |
| Web QoE                        |  web-qoe                    |


Valid values for the `--ungrouped-dimensions` and `--grouped-dimensions` arguments:

| Dimension Description              |  Argument Value                  |
|------------------------------------|----------------------------------|
| ASN                                |  asnum                           |
| Bitrate (kbps)                     |  bitrate-bucket                  |
| Cell                               |  cell                            |
| City                               |  city                            |
| Content Provider ID                |  content-provider-id             |
| Content Provider Name              |  content-provider-name           |
| Continent                          |  continent                       |
| Country                            |  country                         |
| Custom 1                           |  reserved-dim-1                  |
| Custom 2                           |  reserved-dim-2                  |
| Custom 3                           |  reserved-dim-3                  |
| DNS Lookup Time (msec)             |  dns-lookup-time-bucket          |
| Day Part                           |  day-part                        |
| Device Type                        |  device-type                     |
| First Paint Time (seconds)         |  first-paint-time-bucket         |
| Format                             |  format                          |
| HD/SD                              |  hd-sd                           |
| Industry Vertical                  |  industry-vertical               |
| Latitude                           |  latitude                        |
| Longitude                          |  longitude                       |
| Network Operator                   |  network-operator                |
| Network Type                       |  network-type                    |
| Operating System                   |  operating-system                |
| Page Load Time (seconds)           |  page-load-time-bucket           |
| Rebuffer Time Per Minute (seconds) |  rebuffer-time-per-minute-bucket |
| Rebuffers Per Minute               |  rebuffers-per-minute-bucket     |
| Region                             |  region                          |
| Round Trip Time (msec)             |  round-trip-time-bucket          |
| Startup Time (seconds)             |  startup-time-bucket             |
| TCP Connection Time (msec)         |  tcp-connection-time-bucket      |
| Time                               |  time                            |

### Examples

* Generate a time-series report of media KPIs, in CSV format:

    ```bash
    $ akamai nea report \
          --start-time 2018-01-01T05:00:00.000Z \
          --end-time 2018-01-16T04:59:59.999Z \
          --csv \
          --group-id 11111 \
          --network-operator 222 \
          --kpis plays-with-rebuffers startup-time bitrate \
          --ungrouped-dimensions time \
          --report-granularity 3600
    ```

    Output:
    ```
    Getting report... [OK]
    time,Plays with Rebuffers,Startup Time,Bitrate
    2018-01-01T05:00:00.000Z,16.67,1.38,1460.01
    2018-01-01T06:00:00.000Z,14.29,1.36,1416.93
    2018-01-01T07:00:00.000Z,10.46,1.34,1453.75
    2018-01-01T08:00:00.000Z,14.4,1.73,1598.93
    2018-01-01T09:00:00.000Z,13.85,2.21,1640.34
    2018-01-01T10:00:00.000Z,19.8,1.65,1571.03
    2018-01-01T11:00:00.000Z,17.13,2.62,1519.31
    2018-01-01T12:00:00.000Z,9.28,1.72,1475.2
    2018-01-01T13:00:00.000Z,17.42,3.46,1600.78
    ...
    ```

* Generate a time-series report of server KPIs, in JSON format (note that we are piping the output through [jq](https://stedolan.github.io/jq/) to pretty-print the JSON, which is completely optional):

    ```bash
    $ akamai nea report \
        --start-time 2018-01-01T05:00:00.000Z \
        --end-time 2018-01-16T04:59:59.999Z \
        --json \
        --group-id 11111 \
        --network-operator 222 \
        --kpis bandwidth bytes avg-bitrate avg-throughput \
        --ungrouped-dimensions time reserved-dim-2 \
        --report-granularity 3600 | jq '.'
    ```

    Output:
    ```
    Getting report... [OK]
    {
      "kpis": [
        "Bandwidth",
        "Average Throughput",
        "Bytes",
        "Average Bitrate"
      ],
      "series": [
        {
          "dimensions": [],
          "data": [
            [
              "2018-01-01T05:00:00.000Z",
              "Boston",
              258.47,
              14917.89,
              113.58,
              918.04
            ],
            [
              "2018-01-01T05:00:00.000Z",
              "London",
              410.87,
              21661.56,
              180.56,
              802.13
            ],
            ...
          ],
          "maxDate": "2018-01-05T05:00:00.000Z",
          "minDate": "2018-01-04T04:00:00.000Z",
          "avg": 1238.416099009899,
          "min": 47.49,
          "max": 5001.33,
          "percentile2": 492.94120000000004,
          "percentile50": 984.77,
          "percentile98": 3074.9635999999996
        }
      ]
    }
    ```
* Generate a histogram depicting the distribution of media plays over bitrate ranges (note that we are piping the output through [csvlook](http://csvkit.readthedocs.io/en/latest/scripts/csvlook.html) to make the CSV output more readable, which is completely optional):
    ```bash
    $ akamai nea report \
          --start-time 2018-01-01T05:00:00.000Z \
          --end-time 2018-01-16T04:59:59.999Z \
          --csv \
          --group-id 11111 \
          --network-operator 222 \
          --kpis ma-hits \
          --ungrouped-dimensions bitrate-bucket \
          --report-granularity 3600 | csvlook
    ```

    Output:

    ```
    Getting report... [OK]
    | bitrate-bucket      |     Plays |
    | ------------------- | --------- |
    |                     | 1,546,561 |
    | 10:<64.00           |     6,341 |
    | 15:64.00-128.00     |     1,869 |
    | 20:128.00-256.00    |     3,056 |
    | 25:256.00-512.00    |    12,716 |
    | 30:512.00-768.00    |    21,730 |
    | 35:768.00-1024.00   |    30,264 |
    | 40:1024.00-1536.00  |   175,436 |
    | 45:1536.00-2048.00  |    10,078 |
    | 50:2048.00-3072.00  |    49,568 |
    | 55:3072.00-4096.00  |     4,281 |
    | 60:4096.00-6144.00  |     9,894 |
    | 65:6144.00-8192.00  |       331 |
    | 70:8192.00-16384.00 |       453 |
    ```

## Develop

### Run Unit Tests
```
$ cd bin
$ python -m unittest discover
```
