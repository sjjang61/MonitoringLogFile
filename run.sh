#!/bin/sh
APP_HOME=/home/ec2-user/deploy/korail-reservation

function stop(){
	echo 'stop...'
	
	PID=$(ps -ef | grep server.py | grep -v "grep" | awk '{print $2}')
  echo "- pid : ${PID}"
    
	if [[ ! -z $PID ]]; then
		echo "- kill process"
		kill -9 ${PID}
	else
		echo "- no process"
	fi                  
}

function start(){
	echo 'start ...'
	python3 ${APP_HOME}/server.py &
}

function restart(){
	echo 'restart ...'
	stop
	start
}

OPTION=$1

case $OPTION in
                "start")
                start
                ;;

                "stop")
                stop
                ;;
                
                "restart")
                restart
                ;;

        *)
            echo "[usage] : $0 start|stop|restart"
        ;;
esac
