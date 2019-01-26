var monitor = {

    TIME_INTERVAL : 3000,
    MAX_INTERVAL : 100,

    init : function( apiList ){

        console.log("apiList = ", apiList );
        this.apiList = apiList;

        this.initEvent();
        this.initUI();
    },

    initEvent : function(){

        var self = this;

        // 모니터링 요청
        $( "#reqBtn" ).on("click", function(evt){
            self.startMonitor();
            self.toggleMonitor( true );
        });

        // 모니터링 중지
        $( "#stopBtn" ).on("click", function(evt){
            self.stopMonitor(g_interval);
            self.toggleMonitor( false );
        });

        // 서비스 변경
        $("#svc_cd").on( "change", function(evt){
            var svcCd = $(this).val();
            var html = "";

            for( var i = 0 ; i < self.apiList.length ; i++ ){
                if ( self.apiList[i].svc_cd == svcCd ){
                    for( var k = 0 ; k < self.apiList[i].api_list.length ; k++ ){
                        var api = self.apiList[i].api_list[k];
                        html += '<option value='+ api.api_cd + '>' + api.api_nm + '</option>'
                    }
                 }
            }

            $("#api_cd").empty().append( html );
        });
    },

    initUI : function(){
        var svcListHtml = "";
        for( var i = 0 ; i < this.apiList.length ; i++ ){
            svcListHtml += '<option value='+ this.apiList[i].svc_cd + '>' + this.apiList[i].svc_nm + '</option>'
        }
        $("#svc_cd").append( svcListHtml ).trigger("change");
    },

    startMonitor : function(){

        var self = this;

        g_counter = 0;
        g_interval  = setInterval( function(){

            g_counter++;
            console.log( "interval = ", g_counter );
            self.request();

            if( g_counter == this.MAX_INTERVAL ) {
                self.stopMonitor( g_interval );
                self.toggleMonitor( false );
            }
        }, self.TIME_INTERVAL );
    },

    stopMonitor : function( interval ){
        console.log("stop interval");
        clearInterval( interval );
    },

    request : function(){

        var data = $("#form").serializeObject();
        $.ajax({
            url : "/monitor",
            type: "POST",
            data: JSON.stringify( data ) ,
            contentType : "application/json; charset=utf-8",
            //dataType: "json",
            success: function (res) {
                console.log( res );
                var text = $("#monitoring_view").val();
                for( var i = 0 ; i < res.length ; i++ ){
                    text += res[i].file + ' ==> ' + res[i].log;
                }
                $("#monitoring_view").val( text );
            },
            error: function ( xhr, ajaxOptions, thrownError) {
                console.error( "error = " + xhr.status + " " + thrownError);
                alert( "error = " + xhr.status + " " + thrownError);
            }
         });
    },

    toggleMonitor : function( visible ){
        if( visible ){
            $( "#reqBtn" ).hide();
            $( "#stopBtn" ).show();
        }
        else{
            $( "#reqBtn" ).show();
            $( "#stopBtn" ).hide();
        }
    }
}