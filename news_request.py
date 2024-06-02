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
    "query": {
        "$query": {
            "$and": [
                {
                    "$or": [
                        {
                            "sourceLocationUri": "http://en.wikipedia.org/wiki/United_States"
                        },
                        {
                            "sourceLocationUri": "http://en.wikipedia.org/wiki/United_Kingdom"
                        }
                    ]
                }
            ]
        },
        "$filter": {
            "startSourceRankPercentile": 50,
            "endSourceRankPercentile": 100,
            "isDuplicate": "skipDuplicates"
        }
    },
    "apiKey": os.getenv("NEWS_API_KEY")
}