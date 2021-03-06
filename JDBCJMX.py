{
  "version": "1.4",
  "name": "custom.jmx.tomcat.jdbc.pool",
  "type": "JMX",
  "entity": "PROCESS_GROUP_INSTANCE",
  "metricGroup": "tech.tomcat.Connection_Pool",
  "processTypes": [10, 12, 13, 16, 17, 18],
    "configUI" : {
        "displayName": "Tomcat Connection Pool JMX"
    },
  "metrics": [
    {
      "timeseries": {
        "key": "Size",
        "unit": "Count",
	      "displayname": "Size",
        "dimensions": [
          "rx_pid"
        ]
      },
      "source": {
        "domain": "org.apache.tomcat.jdbc.pool.jmx",
        "keyProperties": {
          "name": "dataSourceMBean",
          "type": "ConnectionPool"
        },
        "allowAdditionalKeys": false,
        "attribute": "Size",
        "calculateDelta": false,
        "calculateRate": false,
        "aggregation": "MAX"
      }
    },
    {
      "timeseries": {
        "key": "MaxActive",
        "unit": "Count",
	      "displayname": "MaxActive",
        "dimensions": [
          "rx_pid"
        ]
      },
      "source": {
        "domain": "org.apache.tomcat.jdbc.pool.jmx",
        "keyProperties": {
          "name": "dataSourceMBean",
          "type": "ConnectionPool"
        },
        "allowAdditionalKeys": false,
        "attribute": "MaxActive",
        "calculateDelta": false,
        "calculateRate": false,
        "aggregation": "MAX"
      }
    },
    {
      "timeseries": {
        "key": "Active",
        "unit": "Count",
	      "displayname": "Active",
        "dimensions": [
          "rx_pid"
        ]
      },
      "source": {
        "domain": "org.apache.tomcat.jdbc.pool.jmx",
        "keyProperties": {
          "name": "dataSourceMBean",
          "type": "ConnectionPool"
        },
        "allowAdditionalKeys": false,
        "attribute": "Active",
        "calculateDelta": false,
        "calculateRate": true,
        "aggregation": "MAX"
      }
    }
  ],
    "ui": {
      "charts": [
      {
        "group": "Tomcat JDBC Connection Pool JMX",
        "title": "Connections",
        "series": [
         {
                "key": "MaxActive",
                "displayname": "Max pool size",
                "color": "rgba(101,152,186,0.4)",
                "seriestype": "line"
         },
        {
                "key": "Size",
                "displayname": "Current pool size",
                "seriestype": "area",
                "color" : "#bdc9ff"
        },
         {
                "key": "Active",
                "displayname": "Busy connections",
                "seriestype": "area"
         }
         ]
         }
      ]
    }
}