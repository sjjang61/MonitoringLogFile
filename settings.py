# 서버 API 및 로그 모니터링
apiList = [
    {
        "svc_cd" : "tphone",
        "svc_nm" : "T전화",
        "api_list" : [
            { "api_nm" : "TTS_API", "api_cd" : "api1", "file_path" : "/home/ec2-user/deploy/tts/tts/debug.log" },
            { "api_nm" : "코레일_API", "api_cd" : "api2", "file_path" : "/home/ec2-user/deploy/korail-reservation/debug.log" },
            { "api_nm" : "API3", "api_cd" : "api3", "file_path" : "/3" }
        ]
    },
    {
        "svc_cd" : "phonebook",
        "svc_nm" : "T연락처",
        "api_list" : [
          { "api_nm" : "API4", "api_cd" : "api4", "file_path" : "/4" },
          { "api_nm" : "API5", "api_cd" : "api5", "file_path" : "/5" },
          { "api_nm" : "API6", "api_cd" : "api6", "file_path" : "/6" }
      ]
    } ,
    {
        "svc_cd" : "cloudberry",
        "svc_nm" : "클라우드베리",
        "api_list": [
            {"api_nm": "API7", "api_cd" : "api7", "file_path": "/7"},
            {"api_nm": "API8", "api_cd" : "api8", "file_path": "/8"},
            {"api_nm": "API9", "api_cd" : "api9", "file_path": "/9"}
        ]
    },
    {   
        "svc_cd" : "mkt_tool",
        "svc_nm" : "마케팅툴",
        "api_list": [
            {"api_nm": "API10", "api_cd" : "api10", "file_path": "/10"}
        ]
    }
]

# svc, api 정보 조회
def get_api_info( svc_cd, api_cd ):
    for svc in apiList:
        if svc["svc_cd"] == svc_cd:
            for api in svc["api_list"]:
                if api["api_cd"] == api_cd:
                    return api
    return None




