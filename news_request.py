import os

request_body = {
    "query": {
        "$query": {
            "$and": [
                {
                    "sourceLocationUri": "http://en.wikipedia.org/wiki/United_States"
                },
                {
                    "lang": "eng"
                }
            ]
        },
        "$filter": {
            "dataType": "news",
            "startSourceRankPercentile": 20,
            "endSourceRankPercentile": 100,
            "isDuplicate": "skipDuplicates"
        }
    },
    "apiKey": os.getenv("NEWS_API_KEY")
}

request_body_alt = {
  "$query": {
    "$and": [
      {
        "sourceLocationUri": "http://en.wikipedia.org/wiki/United_States"
      },
      {
        "lang": "eng"
      }
    ]
  },
  "$filter": {
    "hasEvent": "skipArticlesWithoutEvent",
    "startSourceRankPercentile": 70,
    "endSourceRankPercentile": 100,
    "isDuplicate": "skipDuplicates"
  }
}