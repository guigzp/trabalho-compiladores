#!/bin/bash

if [[ $EXEC -eq 1 ]]; then
  # echo 'STARTING EXECUTION' ;
  [[ -n $PATH_LOG ]] || PATH_LOG=run.log
  parallel --tty --verbose --joblog logs/${PATH_LOG}  --jobs $JOBS < /tmp/run2.txt ;
fi
